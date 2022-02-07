from pygame import mixer
import datetime
import time

def timeloop(message,music,stopper) :
    print(message)
    mixer.init()
    mixer.music.load(music)
    mixer.music.play()
    while True :
        stop = input()
        if stop == "done" :
            mixer.music.pause()
            with open("E:\manager.txt","a") as f :
                do = stopper + "    " + str(datetime.datetime.now()) + "\n"
                f.write(do)
            break
        else :
            continue


if __name__ == '__main__' :
    with open("E:\manager.txt", "a") as f:
        do = "\n" + str(datetime.date.today()) + "\n\n"
        f.write(do)
    time_water = time.time()
    time_eyes = time.time()
    time_ex = time.time()
    while True :
        if  time.time() - time_water > 3600 :
            timeloop("Time to drank water. To stop type 'done'.","water.mp3","water drank")
            time_water = time.time()
            time_eyes = time.time()
        elif  time.time() - time_eyes > 1800 :
            timeloop("Time to relax your eyes. To stop type 'done'.","eyes.mp3","eyes relaxed")
            time_eyes = time.time()
        elif time.time() - time_ex > 7200:
            timeloop("Time to exercise. To stop type 'done'.", "exercise.mp3", "Exercise done")
            time_eyes = time.time()
            time_water = time.time()
            time_eyes = time.time()


