{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kianpey/Hello/blob/main/zarb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eRFa550Xs0i1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "58820beb-9ea6-4510-e4f9-fd57be2d85d8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "4 × 0 = 0\n",
            "4 × 1 = 4\n",
            "4 × 2 = 8\n",
            "4 × 3 = 12\n",
            "4 × 4 = 16\n",
            "4 × 5 = 20\n",
            "4 × 6 = 24\n",
            "4 × 7 = 28\n",
            "4 × 8 = 32\n",
            "4 × 9 = 36\n",
            "4 × 10 = 40\n",
            "hello\n"
          ]
        }
      ],
      "source": [
        "num=int(input())\n",
        "for i in range(0,11):\n",
        "  print(num,\"×\",i,\"=\",num*i)\n"
      ]
    }
  ]
}