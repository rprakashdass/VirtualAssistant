# ### Advanced Input Output Statement Problems

"""
# 1. **Lowercase Lines**: Write a Python program that accepts a sequence of lines (blank line to terminate) as input
 and prints the lines as output (all characters in lower case).
"""


def Lowercase_lines():
    print(input())


# Lowercase_lines()

# 2. **Fibonacci Numbers**: Write a Python program that accepts a number N and prints the first N Fibonacci numbers.

def Fibonacci_numbers():
    N = int(input('Enter the number N'))
    a,b = 0,1
    series = 0
    print(a, b, end=' ')
    for i in range(0, N):
        series = a+b
        a = b
        b = series
        print(series,end=' ')


# Fibonacci_numbers()

# 3. **Vowel Count**: Write a Python program that accepts a string and prints the number of vowels in the string.


def Vowel_Count():
    string = input('Input the string')
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for i in range(0, len(string)):
        for j in range(0, len(vowels)):
            if string[i] == vowels[j]:
                vowel_count = vowel_count + 1
    print(vowel_count)


Vowel_Count()
# 4. **Consonant Count**: Write a Python program that accepts a string and prints the number of consonants in the string.
#
# 5. **Digit Count**: Write a Python program that accepts a string and prints the number of digits in the string.
#
# 6. **Word Count**: Write a Python program that accepts a string and prints the number of words in the string.
#
# 7. **Unique Characters**: Write a Python program that accepts a string and prints the number of unique characters in the string.
#
# 8. **Reverse String**: Write a Python program that accepts a string and prints the reverse of the string.
#
# 9. **Longest Common Substring**: Write a Python program that accepts two strings and prints the longest common substring between the two strings.
#
# 10. **Number Matrix**: Write a Python program that accepts a number N and prints an NxN matrix of numbers from 1 to N^2.
#
# 11. **Spiral Matrix**: Write a Python program that accepts a number N and prints an NxN spiral matrix of numbers from 1 to N^2.
#
# 12. **Checkerboard Matrix**: Write a Python program that accepts a number N and prints an NxN checkerboard matrix of numbers from 1 to N^2.
#
# 13. **Sierpinski Triangle**: Write a Python program that accepts a number N and prints an NxN Sierpinski triangle.
#
# 14. **Mandelbrot Set**: Write a Python program that accepts a number N and prints an NxN Mandelbrot set.
#
# 15. **Julia Set**: Write a Python program that accepts a number N and prints an NxN Julia set.
#
# 16. **Koch Snowflake**: Write a Python program that accepts a number N and prints an NxN Koch snowflake.
#
# 17. **Sierpinski Carpet**: Write a Python program that accepts a number N and prints an NxN Sierpinski carpet.
#
# 18. **Menger Sponge**: Write a Python program that accepts a number N and prints an NxN Menger sponge.
#
# 19. **Hilbert Curve**: Write a Python program that accepts a number N and prints an NxN Hilbert curve.
#
# 20. **Peano Curve**: Write a Python program that accepts a number N and prints an NxN Peano curve.
#
# Feel free to explore these programs, modify them, and learn from the explanations provided.
#
# ## Topics
#
# In addition to the programs, this repository also covers various Python topics such as control flow, data structures, file handling, string manipulation, and more. You can find detailed explanations, examples, and exercises on these topics to enhance your Python skills.
#
# Start exploring the repository and have fun learning Python!
#
