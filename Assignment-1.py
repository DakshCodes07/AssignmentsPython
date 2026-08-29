{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e94d3e83-773e-4f66-ad20-df749867a6f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List: ['Daksh', 'Utkarsh', 'Siddhesh', 'Soham']\n"
     ]
    }
   ],
   "source": [
    "#Lists\n",
    "\n",
    "students = [\"Daksh\", \"Utkarsh\",\"Siddhesh\", \"Soham\"]\n",
    "print(\"Original List:\", students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d5388fcd-214e-40dd-a2fc-93e2176e9249",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After append('Jitesh'): ['Daksh', 'Utkarsh', 'Siddhesh', 'Soham', 'Jitesh']\n"
     ]
    }
   ],
   "source": [
    "students.append(\"Jitesh\")\n",
    "print(\"After append('Jitesh'):\", students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e2892c8b-6160-417c-8e01-a86b9be63127",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After insert(1, 'Daksh'): ['Arnav', 'Daksh', 'Arnav', 'Utkarsh', 'Siddhesh', 'Soham', 'Jitesh']\n"
     ]
    }
   ],
   "source": [
    "students.insert(1, \"Daksh\")\n",
    "print(\"After insert(1, 'Daksh'):\", students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3a68ed0e-518c-4c35-841e-7f3263c7ed43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After remove('Arnav'): ['Daksh', 'Arnav', 'Utkarsh', 'Siddhesh', 'Soham', 'Jitesh']\n"
     ]
    }
   ],
   "source": [
    "students.remove(\"Arnav\")\n",
    "print(\"After remove('Arnav'):\", students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f1e0e23d-62e7-4aa3-8c70-b0d25aa3b425",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After sort(): ['Arnav', 'Daksh', 'Jitesh', 'Siddhesh', 'Soham', 'Utkarsh']\n"
     ]
    }
   ],
   "source": [
    "students.sort()\n",
    "print(\"After sort():\", students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2e5a4aaf-bbf6-4a20-8b34-4e9d7ab16b5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Tuple: ('Daksh', 'Utkarsh', 'Siddhesh', 'Soham')\n"
     ]
    }
   ],
   "source": [
    "#Tuple\n",
    "\n",
    "student_tuple = (\"Daksh\", \"Utkarsh\", \"Siddhesh\", \"Soham\")\n",
    "print(\"Original Tuple:\", student_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5d1fa41c-3fd1-40e3-aaf2-10601a9b2856",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count('Daksh'): 1\n"
     ]
    }
   ],
   "source": [
    "count_Daksh = student_tuple.count(\"Daksh\")\n",
    "print(\"count('Daksh'):\", count_Daksh)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "85c90d91-7e7e-4cae-b7d4-70194b7a2d5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "index('Soham): 3\n"
     ]
    }
   ],
   "source": [
    "index_Soham = student_tuple.index(\"Soham\")\n",
    "print(\"index('Soham):\", index_Soham)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "490205d0-3d71-4782-8f71-7b783cb12c5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Slicing [1:3]: ('Utkarsh', 'Siddhesh')\n"
     ]
    }
   ],
   "source": [
    "sliced = student_tuple[1:3]\n",
    "print(\"Slicing [1:3]:\", sliced)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7d33b211-6369-4c50-9152-0c7dbc48f517",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Concatenation (+): ('Daksh', 'Utkarsh', 'Siddhesh', 'Soham', 'Arnav', 'Rachit')\n"
     ]
    }
   ],
   "source": [
    "new_tuple = student_tuple + (\"Arnav\", \"Rachit\")\n",
    "print(\"Concatenation (+):\", new_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "01758794-e1bc-4860-9dbb-2d0dfc03e340",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unpacked values: Daksh Utkarsh Siddhesh Soham\n"
     ]
    }
   ],
   "source": [
    "student_tuple = (\"Daksh\", \"Utkarsh\", \"Siddhesh\", \"Soham\")\n",
    "a, b, c, d = student_tuple\n",
    "print(\"Unpacked values:\", a, b, c, d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e48bfb51-d924-4674-8255-76727919c476",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Dictionary {101: 'daksh', 102: 'soham', 103: 'utkarsh', 104: 'bajaj'}\n"
     ]
    }
   ],
   "source": [
    "#Dictionary\n",
    "student_dict ={101: \"daksh\", 102: \"soham\", 103: \"utkarsh\", 104: \"bajaj\"}\n",
    "print(\"Original Dictionary\", student_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ffb0bb45-875a-406b-84f9-efc99aa46ea0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "keys(): [101, 102, 103, 104]\n"
     ]
    }
   ],
   "source": [
    "print(\"keys():\", list(student_dict.keys()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e582a05c-9811-4ce8-a001-2e893e868637",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "values(): ['daksh', 'soham', 'utkarsh', 'bajaj']\n"
     ]
    }
   ],
   "source": [
    "print(\"values():\", list(student_dict.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9e598008-8861-4e4e-9f99-cdb785172652",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "items(): [(101, 'daksh'), (102, 'soham'), (103, 'utkarsh'), (104, 'bajaj')]\n"
     ]
    }
   ],
   "source": [
    "print(\"items():\", list(student_dict.items()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5f222750-e184-498a-8e8d-394e5b0366cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After update({105: 'jitesh'}): {101: 'daksh', 102: 'soham', 103: 'utkarsh', 104: 'bajaj', 105: 'jitesh'}\n"
     ]
    }
   ],
   "source": [
    "student_dict.update({105: \"jitesh\"})\n",
    "print(\"After update({105: 'jitesh'}):\", student_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0c9034a-c44a-43ca-b28d-09ba1035471f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
