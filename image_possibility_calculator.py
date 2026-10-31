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

print("\npossible conditions ** pixel")

if digits <= 1000:
    totalPossibleConditions = conditionsPerPixel ** totalPixels
    print("Total possible conditions:", totalPossibleConditions)

else:
    print("Log10 of total possible conditions:", logConditions)
    print("Digits in total possible conditions:", digits)


bits = float(totalPixels) * float(bits) * float(channels)
print("\nTotal information per image: ", bits, "bits")

bytes = bits / 8
kilobytes = bytes / 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024
terabytes = gigabytes / 1024

print("Bytes:\t", round(bytes, 3))
print("KBs:\t", round(kilobytes, 3))
print("MBs:\t", round(megabytes, 3))
print("GBs:\t", round(gigabytes, 3))
print("TBs:\t", round(terabytes, 3))

if megabytes > 10:
    print("\nKeep in mind that these are uncompressed values")

logTotalStorage = math.log10(terabytes) + (bits * math.log10(2))
digits = math.floor(logTotalStorage) + 1

print("\nsize * possible conditions")
print("Log10 of total terabytes:", logTotalStorage)
print("Digits in total terabytes:", digits)