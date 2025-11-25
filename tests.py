# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestFileInfo(unittest.TestCase):

    def test_current(self):
        print("Result for current directory:")
        result = get_files_info("calculator", ".")
        print(result)
        for line in result.splitlines():
            if len(line.strip()) == 0:
                continue
            self.assertEqual(line.lstrip().startswith("- "), True)
            self.assertEqual("file_size" in line, True)
            self.assertEqual(" bytes" in line, True)
            self.assertEqual("is_dir=" in line, True)
    
    def test_pkg(self):
        print("Result for current directory:")
        result = get_files_info("calculator", "pkg")
        print(result)
        for line in result.splitlines():
            if len(line.strip()) == 0:
                continue
            self.assertEqual(line.lstrip().startswith("- "), True)
            self.assertEqual("file_size" in line, True)
            self.assertEqual(" bytes" in line, True)
            self.assertEqual("is_dir=" in line, True)
    
    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')
    
    def test_error(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()