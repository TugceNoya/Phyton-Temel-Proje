{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "A = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "def flatten(inList):\n    flattened_list = []\n    for item in inList:\n        if type(item) == type([]):\n            flattened_list.extend(flatten(item))\n        else:\n            flattened_list.append(item)\n    return flattened_list\n    ",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "flatten(A)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 102,
      "outputs": [
        {
          "execution_count": 94,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[1, 'a', 'cat', 2, 3, 'dog', 4, 5]"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "B= [[1, 2], [3, 4], [5, 6, 7]]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "B",
      "metadata": {
        "trusted": true
      },
      "execution_count": 29,
      "outputs": [
        {
          "execution_count": 26,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[1, 2], [3, 4], [5, 6, 7]]"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "def rev(inList):\n    C=[]\n    for e in inList:\n        if type(e) == type ([]):\n            C.append(e[::-1])   \n    return C[::-1]     ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "rev(B)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 101,
      "outputs": [
        {
          "execution_count": 93,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[7, 6, 5], [4, 3], [2, 1]]"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    }
  ]
}