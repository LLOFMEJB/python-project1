{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center><img src=\"https://github.com/aaron-clarusway/fullstack/blob/master/itf-logo.png?raw=true\"  alt=\"alt text\" width=\"200\"/></center>\n",
    "<br>\n",
    "<h1><p style=\"text-align: center; color:darkblue\">Python Basic & Plus</p><h1>\n",
    "<center><h1>Workshop - 3</h1></center>\n",
    "<p><img align=\"right\"\n",
    "  src=\"https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg\"  width=\"15px\"></p>\n",
    "<br>\n",
    "\n",
    "\n",
    "# Subject: Collections - Control Flow Statements - Functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Coding Challenge -1 : Validate Combination of Brackets\n",
    "\n",
    "Purpose of the this coding challenge is to solve a combination problem using loops.\n",
    "\n",
    "### Learning Outcomes\n",
    "\n",
    "At the end of the this coding challenge, students will be able to;\n",
    "\n",
    "- understand the use of loops.\n",
    "- solve the advanced and complicated problems.\n",
    "- understand the importance of pattern recognition.\n",
    "- get a better understanding in manipulating lists or strings.\n",
    "\n",
    "### Problem Statement\n",
    "  \n",
    "- Write a function that given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determines if the input string is valid or not by using following rules.\n",
    "\n",
    "- An input string is valid if:\n",
    "\n",
    "  - Open brackets must be closed by the same type of brackets.\n",
    "\n",
    "  - Open brackets must be closed in the correct order.\n",
    "\n",
    "- Note that an empty string is also considered valid.\n",
    "\n",
    "- Example for user inputs and respective outputs\n",
    "\n",
    "```bash\n",
    "Input        Output\n",
    "--------:    ------:\n",
    "\"()\"         True\n",
    "\"()[]{}\"     True\n",
    "\"(]\"         False\n",
    "\"([)]\"       False\n",
    "\"{[]}\"       True\n",
    "\"\"           True\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ([[])}\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def isValid(s):\n",
    "    bracket_map = {\"(\": \")\", \"[\": \"]\",  \"{\": \"}\"}\n",
    "    open_par = set([\"(\", \"[\", \"{\"])\n",
    "    stack = []\n",
    "    for i in s:\n",
    "        if i in open_par:\n",
    "            stack.append(i)\n",
    "        elif stack and i == bracket_map[stack[-1]]:\n",
    "            stack.pop()\n",
    "        else:\n",
    "            return False\n",
    "    return stack == []\n",
    "\n",
    "combination = input('Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ')\n",
    "print(isValid(combination))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Coding Challenge - 2: Calculate Stock Profit\n",
    "\n",
    "The purpose of this coding challenge is to write a program that calculates maximum profit you could get from a stock.\n",
    "\n",
    "### Learning Outcomes\n",
    "\n",
    "At the end of this coding challenge, students will be able to;\n",
    "\n",
    "- analyze a problem, identify, and apply programming knowledge for appropriate solution.\n",
    "\n",
    "- design, implement `arithmetic operators` effectively in Python to solve the given problem.\n",
    "\n",
    "- demonstrate their knowledge of algorithmic design principles by solving the problem effectively.\n",
    "\n",
    "### Problem Statement\n",
    "\n",
    "Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.\n",
    "\n",
    "For example, given ``[9, 11, 8, 5, 7, 10]``, you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.\n",
    "\n",
    "Example of different list of stock prices and respective outputs.\n",
    "\n",
    "```bash\n",
    "List = [75,73,60,100,120,130]\n",
    "Output = 70\n",
    "List = [10,20,23,22,17,30]\n",
    "Output = 20\n",
    "List = [1,6,19,59,30,60]\n",
    "Output = 59\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution-1 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def buy_and_sell(arr):\n",
    "    max_profit = 0\n",
    "    for i in range(len(arr) - 1):\n",
    "        for j in range(i, len(arr)):\n",
    "            buy_price, sell_price = arr[i], arr[j]\n",
    "            max_profit = max(max_profit, sell_price - buy_price)\n",
    "    return max_profit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "77"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "buy_and_sell([1,45,6,78,9])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution-2 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def buy_and_sell(arr):\n",
    "    current_max, max_profit = 0, 0\n",
    "    for price in reversed(arr):\n",
    "        current_max = max(current_max, price)\n",
    "        potential_profit = current_max - price\n",
    "        max_profit = max(max_profit, potential_profit)\n",
    "    return max_profit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "44"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "buy_and_sell([22,33,44,55,66])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Coding Challenge - 3: Morse Translator\n",
    "\n",
    "The purpose of this coding challenge is to write a program that translates the plain text to morse code.\n",
    "\n",
    "### Learning Outcomes\n",
    "\n",
    "At the end of this coding challenge, students will be able to;\n",
    "\n",
    "- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.\n",
    "\n",
    "- Implement loops to solve a problem.\n",
    "\n",
    "- Make use of dictionary data structure to map values. \n",
    "\n",
    "- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.\n",
    "\n",
    "### Problem Statement\n",
    "\n",
    "Write a function that takes in a plain text as input and converts it into morse alphabet. Following alphabet can be used:\n",
    "\n",
    "```bash\n",
    "{\n",
    "  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',\n",
    "  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',\n",
    "  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',\n",
    "  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',\n",
    "  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',\n",
    "  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',\n",
    "  '6': '-....', '7': '--...', '8': '---..', '9': '----.',\n",
    "  '&': '.-...', \"'\": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',\n",
    "  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',\n",
    "  '-': '-....-', '+': '.-.-.', '\"': '.-..-.', '?': '..--..', '/': '-..-.'\n",
    "}\n",
    "```\n",
    "- Expected Outputs:\n",
    "\n",
    "```bash\n",
    "Input: Hello world!\n",
    "\n",
    "Output:\n",
    ".... . .-.. .-.. ---   .-- --- .-. .-.. -.. -.-.--\n",
    "\n",
    "Input: Good job!\n",
    "\n",
    "Output: --. --- --- -..   .--- --- -... -.-.--\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def encode_morse(message):\n",
    "\tchar_to_dots = {\n",
    "  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',\n",
    "  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',\n",
    "  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',\n",
    "  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',\n",
    "  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',\n",
    "  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',\n",
    "  '6': '-....', '7': '--...', '8': '---..', '9': '----.',\n",
    "  '&': '.-...', \"'\": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',\n",
    "  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',\n",
    "  '-': '-....-', '+': '.-.-.', '\"': '.-..-.', '?': '..--..', '/': '-..-.'\n",
    "\t}\n",
    "\tresult = \"\"\n",
    "\tfor c in message:\n",
    "\t\tresult += char_to_dots[c.upper()] + \" \"\n",
    "\treturn result[:len(result)-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'-.-. .-.. .- .-. ..- ... .-- .- -.--'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encode_morse(\"clarusway\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
