{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter your name: Selin\n",
      "Please enter your surname: Ünlü\n",
      "Welcome\n",
      "Please enter your number of Course4\n",
      "Midterm: 23\n",
      "Final: 44\n",
      "Project: 77\n"
     ]
    }
   ],
   "source": [
    "name = \"Selin\"\n",
    "surname =\"Ünlü\"    \n",
    "\n",
    "Control=True\n",
    "\n",
    "for i in range(3):\n",
    "    name1 = input(\"Please enter your name: \")\n",
    "    surname1 = input(\"Please enter your surname: \")\n",
    "    \n",
    "    if(name == name1 and surname == surname1):   \n",
    "        print(\"Welcome\")\n",
    "        Control_=True\n",
    "        break    \n",
    "    else:\n",
    "        Control_=False\n",
    "                \n",
    "if not Control_:\n",
    "        print(\"Please try again later!\") \n",
    "        pass\n",
    "else:\n",
    "    numberLesson = int(input(\"Please enter your number of Course\"))\n",
    "    \n",
    "    if(numberLesson<3):\n",
    "        print(\"You failed in class\")\n",
    "        \n",
    "    else:\n",
    "        \n",
    "        midterm = float(input(\"Midterm: \"))\n",
    "        final   = float(input(\"Final: \"))\n",
    "        project = float(input(\"Project: \"))\n",
    "\n",
    "        average = 0.3*midterm + 0.5*final + 0.2*project \n",
    "    \n",
    "        def noteCalc(average_):\n",
    "\n",
    "            if average_<30:\n",
    "                grade=\"EE\"\n",
    "                return(\"She/He failed with {}\".format(grade))\n",
    "        \n",
    "            else:\n",
    "                if average_ > 90:\n",
    "                    grade=\"AA\"\n",
    "                elif 70<average_<=90:\n",
    "                    grade=\"BB\"\n",
    "                elif 50<average_<=70:\n",
    "                    grade=\"CC\"\n",
    "                else:\n",
    "                    grade=\"DD\"\n",
    "                    return(\"She/He is successful with {}\".format(grade)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'She/He is successful with DD'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "noteCalc(average)"
   ]
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
