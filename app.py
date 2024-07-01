"""
Few Notes:
1. Dictionary in Python is mutable.
2. The code coveres both uppercase and Lowercase commands.
3. Before running each command it checks if the command is valid or not.
"""


class FolderStructure:
    """
    FolderStructure class to create, delete, move and list folders and subfolders.

    """

    def __init__(self):
        """
        Constructor to initialize the root folder.
        """
        self.root = {}

    def create(self, path):
        """
        Create a folder or subfolder.

        Args:
            path (str): The path of the folder or subfolder to be created.

        Returns:
            None
        """
        folders = path.split("/")
        _root = self.root
        for folder in folders:
            if folder not in _root:
                _root[folder] = {}
            _root = _root[folder]

    def delete(self, params):
        """
        Delete a folder or subfolder.

        Args:
            params (str): The path of the folder or subfolder to be deleted.

        Returns:
            None
        """
        folders = params.split("/")
        _root = self.root
        folders_length = len(folders)
        for i in range(folders_length):
            if folders[i] in _root:
                if i == folders_length - 1:
                    del _root[folders[i]]
                else:
                    _root = _root[folders[i]]
            else:
                print(f"Cannot delete {params} - {folders[i]} does not exist")
                break

    def move(self, source, destination):
        """
        Move a folder or subfolder from one location to another.

        Args:
            source (str): The path of the folder or subfolder to be moved.
            destination (str): The path of the destination folder or subfolder.

        Returns:
            None
        """

        # This is not requested but we can create the destination folder if it does not exist.
        self.create(destination)

        destination_root = self.root
        desination_folders = destination.split("/")
        # traverse to the destination folder
        for folder in desination_folders:
            destination_root = destination_root[folder]

        source_folders = source.split("/")
        _root = self.root

        # traverse to the source folder
        source_folders_length = len(source_folders)
        for i in range(source_folders_length):
            if i == source_folders_length - 1:
                moving_item = source_folders[i]
            else:
                _root = _root[source_folders[i]]

        destination_root[moving_item] = _root[source_folders[i]]
        del _root[source_folders[i]]

    def show_list(self):
        """
        Call the show_list method recursively.

        Args:
            None

        Returns:
            None
        """
        self.show_list_recursive(self.root)

    def show_list_recursive(self, dict_of_folders, depth=0):
        """
        Display the folders in hierarchical structure.

        Args:
            path (dict): The file system structure to be displayed.
            depth (int): The depth of the current folder or subfolder.

        Returns:
            None
        """
        for k, v in sorted(dict_of_folders.items()):
            print("  " * depth + k)
            if isinstance(v, dict):
                self.show_list_recursive(v, depth + 1)


if __name__ == '__main__':
    print("Enter your commands. Ctrl-D or Ctrl+Z (windows) to run them.")
    inputs = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        inputs.append(line)
    print("#################################")
    fs = FolderStructure()
    for content in inputs:
        # Skip empty lines
        if not content:
            continue

        # Print the Command
        print(content)
        input_line_parts = content.split(" ")

        command = input_line_parts[0].upper()
        if command == "CREATE":
            if len(input_line_parts) < 2:
                print("Invalid CRETE command. Please provide a path.")
                continue
            fs.create(input_line_parts[1])

        elif command == "LIST":
            fs.show_list()

        elif command == "MOVE":
            if len(input_line_parts) < 3:
                print(
                    "Invalid MOVE command. Please provide source and destination path.")
                continue
            fs.move(input_line_parts[1], input_line_parts[2])

        elif command == "DELETE":
            if len(input_line_parts) < 2:
                print("Invalid DELETE command. Please provide a path.")
                continue
            fs.delete(input_line_parts[1])

        else:
            print("Invalid Command")
