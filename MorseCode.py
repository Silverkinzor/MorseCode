import wave, struct, math

print("Morse Code Converter")
print("by: Matthew Le Huenen")
print("---------------------")
print("")

while True:

    # --- Wave Output Function derived from public example at http://blog.acipo.com/wave-generation-in-python/ ---
    def waveOutput(duration, sampleRate, frequency, file):
        for i in range(int(duration * sampleRate)):
            value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sampleRate)))
            data = struct.pack('<h', value)
            file.writeframesraw( data )
    # ------------------------------------------------------------------------------------------------------------

    # set morse tone frequencies and durations

    sampleRate = 8000.0      # hertz (set to 44100 for CD quality)

    baseFrequency = 1000.0   # frequency of tone in hertz
    emptyFrequency = 0.0     # no tone

    dotDuration = 0.25       # durations in seconds
    dashDuration = 0.75
    emptyDuration = 0.25

    # morseList contains morse code characters for each alphabetic letter
    # morseList[0] == 'a', morseList[1] == 'b', morseList[2] == 'c' ... morseList[25] == 'z'

    morseList = [ ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                  "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                  "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                  "-.--", "--.." ]

    # morseNumericList contains morse code characters for each number
    # morseNumericList[0] == 0, morseNumericList[1] == 1 ... morseNumericList[9] == 9

    morseNumericList =  [ "-----", ".----", "..---", "...--", "....-", 
                          ".....", "-....", "--...", "---..", "----." ]

    # user input from console

    morseInputString = input("Enter text to convert to Morse code: ")

    # convert user input to lowercase, as Morse code does not distinguish between upper and lowercase

    morseInputString = morseInputString.lower()

    # open morse code sound file using user input as filename

    wavef = wave.open(morseInputString + ".wav", 'w')
    wavef.setnchannels(1)   # mono
    wavef.setsampwidth(2) 
    wavef.setframerate(sampleRate)

    # loop through morse string user input

    for i in range(0, len(morseInputString)):
        if (morseInputString[i] == ' '):
            morseOutput = ""
            waveOutput(emptyDuration * 2, sampleRate, emptyFrequency, wavef)

        elif (morseInputString[i].isdigit()):
            morseOutput = morseNumericList[int(morseInputString[i])]

        else:
            # Convert character at morseString index position 'i' to morseList index position via ASCII code

            morseListIndex = ord(morseInputString[i]) - 97
            morseOutput = morseList[morseListIndex]

        # display Morse code sequence to console output

        print(morseInputString[i], ":", morseOutput)

        # loop inner characters of morse code character

        for j in range(0, len(morseOutput)):

            # handle Morse dot

            if (morseOutput[j] == '.'):
                waveOutput(dotDuration, sampleRate, baseFrequency, wavef)

            # handle Morse dash

            if (morseOutput[j] == '-'):
                waveOutput(dashDuration, sampleRate, baseFrequency, wavef)

            # add small duration silence between Morse code characters

            waveOutput(emptyDuration, sampleRate, emptyFrequency, wavef)

        # add longer duration silence between input string characters

        waveOutput(emptyDuration * 2, sampleRate, emptyFrequency, wavef)

    # Close Morse code sound file

    wavef.close()

    try_again = int(input("Press 1 to run the program again, 0 to exit. ")) # Ask the user if they wish to re-run the program
    if try_again == 0:
        break # break out of the outer while loop