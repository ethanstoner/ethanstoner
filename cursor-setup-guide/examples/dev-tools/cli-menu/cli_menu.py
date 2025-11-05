#!/usr/bin/env python3
"""
CLI Menu System
Interactive command-line menu for running tools and presets.
"""

import os
import sys
import subprocess
from typing import List, Optional, Callable


class MenuItem:
    """Menu item with label and action."""
    
    def __init__(self, label: str, action: Optional[Callable] = None, command: Optional[str] = None):
        """
        Args:
            label (str): Display label
            action (callable, optional): Function to call
            command (str, optional): Shell command to run
        """
        self.label = label
        self.action = action
        self.command = command
    
    def execute(self):
        """Execute the menu item action."""
        if self.action:
            return self.action()
        elif self.command:
            try:
                result = subprocess.run(
                    self.command,
                    shell=True,
                    check=False
                )
                return result.returncode == 0
            except Exception as e:
                print(f"Error executing command: {e}")
                return False
        return True


class Menu:
    """Interactive CLI menu."""
    
    def __init__(self, title: str, items: List[MenuItem]):
        """
        Args:
            title (str): Menu title
            items (list): List of MenuItem objects
        """
        self.title = title
        self.items = items
        self.selected_index = 0
    
    def display(self):
        """Display the menu."""
        # Clear screen (cross-platform)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\n{'=' * 50}")
        print(f"  {self.title}")
        print(f"{'=' * 50}\n")
        
        for i, item in enumerate(self.items):
            marker = "> " if i == self.selected_index else "  "
            print(f"{marker}{i + 1}. {item.label}")
        
        print("\n" + "=" * 50)
        print("Use arrow keys to navigate, Enter to select, 'q' to quit")
    
    def run(self):
        """Run the interactive menu."""
        try:
            import termios
            import tty
            
            # Unix-like systems
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            
            try:
                tty.setraw(sys.stdin.fileno())
                
                while True:
                    self.display()
                    
                    # Read key
                    key = sys.stdin.read(1)
                    
                    if key == '\x1b':  # Escape sequence
                        key += sys.stdin.read(2)
                        if key == '\x1b[A':  # Up arrow
                            self.selected_index = (self.selected_index - 1) % len(self.items)
                        elif key == '\x1b[B':  # Down arrow
                            self.selected_index = (self.selected_index + 1) % len(self.items)
                    elif key == '\r' or key == '\n':  # Enter
                        item = self.items[self.selected_index]
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if item.label.lower() == "exit" or item.command is None:
                            break
                        print(f"\nExecuting: {item.label}\n")
                        item.execute()
                        input("\nPress Enter to continue...")
                    elif key == 'q':
                        break
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        except (ImportError, OSError):
            # Fallback for Windows or systems without termios
            self._run_simple()
    
    def _run_simple(self):
        """Simple menu runner for Windows."""
        while True:
            self.display()
            
            try:
                choice = input("\nEnter choice (1-{} or 'q' to quit): ".format(len(self.items)))
                
                if choice.lower() == 'q':
                    break
                
                index = int(choice) - 1
                if 0 <= index < len(self.items):
                    item = self.items[index]
                    if item.label.lower() == "exit" or item.command is None:
                        break
                    print(f"\nExecuting: {item.label}\n")
                    item.execute()
                    input("\nPress Enter to continue...")
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
            except (ValueError, KeyboardInterrupt):
                break


if __name__ == "__main__":
    # Example usage
    def hello_world():
        print("Hello, World!")
        return True
    
    items = [
        MenuItem("Option 1: Hello World", action=hello_world),
        MenuItem("Option 2: List Files", command="ls -la"),
        MenuItem("Option 3: Show Date", command="date"),
        MenuItem("Exit", None)
    ]
    
    menu = Menu("Example Menu", items)
    menu.run()

