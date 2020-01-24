import tweety
import json

class judge():
    def __init__(self, handle, count):
        self.handle = handle
        self.count = count

    def analyzer(self):
        self.analysis = {
            "handle" : self.handle,
            "count" : self.count
        }
        out = json.loads(tweety.get_tweets(self.handle, self.count))
        index = 0
        for item in out:
            data = {
                "length" : len(out[item]['text'])
            }
            
            self.analysis[index] = data
            index += 1

    def go(self):
        self.analyzer()
        pass

if __name__ == "__main__":
    judge = judge('realDonaldTrump', 5)
    judge.go()
    print(judge.analysis)