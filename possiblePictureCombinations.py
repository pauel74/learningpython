import os
import math
os.system("clear")

resolutionHeight = input("Enter pixel height: ")
print("\nEnter aspect ratio")
aspectRatioX = input("width: ")
aspectRatioY = input("height: ")

aspectRatio = float(aspectRatioX) / float(aspectRatioY)
print("\nAspect ratio: ", round(aspectRatio,3))

resolutionWidth = float(resolutionHeight) * aspectRatio
print("Pixel width: ", round(resolutionWidth))

totalPixels = float(resolutionWidth) * float(resolutionHeight)
print("Total pixels: ", round(totalPixels))

print("\nColor Space")
bits = input("Bits: ")
channels = input("Channels: ")

conditionsPerPixel = 2 ** float(bits)
conditionsPerPixel **= float(channels)
print("\nPossible conditions per pixel: ", round(conditionsPerPixel))

logConditions = totalPixels * math.log10(conditionsPerPixel)
digits = math.floor(logConditions) + 1

if digits <= 1000:
    totalPossibleConditions = conditionsPerPixel ** totalPixels
    print("Total possible conditions:", totalPossibleConditions)

else:
    print("\nLog10 of total possible conditions:", logConditions)
    print("Digits in total possible conditions:", digits)