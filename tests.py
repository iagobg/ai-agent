from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    # print(get_file_content("calculator","lorem.txt"))
    
    # # Test 1: List current directory in calculator
    # print("Result for current directory:")
    # result1 = get_files_info("calculator", ".")
    # print(result1)
    # print()
    
    # # Test 2: List pkg subdirectory
    # print("Result for 'pkg' directory:")
    # result2 = get_files_info("calculator", "pkg")
    # print(result2)
    # print()
    
    # # Test 3: Try to access /bin (should fail)
    # print("Result for '/bin' directory:")
    # result3 = get_files_info("calculator", "/bin")
    # print(result3)
    # print()
    
    # # Test 4: Try to access parent directory (should fail)
    # print("Result for '../' directory:")
    # result4 = get_files_info("calculator", "../")
    # print(result4)

    # print("Result for current directory:")
    # result1 = get_file_content("calculator", "main.py")
    # print(result1)
    # print()
    
    # # Test 2: List pkg subdirectory
    # print("Result for 'pkg' directory:")
    # result2 = get_file_content("calculator", "pkg/calculator.py")
    # print(result2)
    # print()
    
    # # Test 3: Try to access /bin (should fail)
    # print("Result for '/bin' directory:")
    # result3 = get_file_content("calculator", "/bin")
    # print(result3)
    # print()
    
    # # Test 4: Try to access parent directory (should fail)
    # print("Result for '../' directory:")
    # result4 = get_file_content("calculator", "../")
    # print(result4)

    # print(write_file("calculator","lorem.txt","wait, this isn't lorem ipsum"))
    # print(write_file("calculator","morelorem.txt","lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    main()