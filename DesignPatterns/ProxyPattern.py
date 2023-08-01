
# proxy pattern

# structural design pattern

# client --> request for service -- ServiceProviderClass

# Proxy
    # caching
    # logging
    # access control
    # post processing
    

from abc import ABC, abstractmethod

class VideoDownloader(ABC):

    @abstractmethod
    def downloadVideo(self, videoName):
        pass


class TPVideoDownloader(VideoDownloader):

    def downloadVideo(self, videoName):
        return f'Downloaded {videoName}'
    
class Proxy(VideoDownloader):

    __cache = {}

    def __init__(self, videoDownloader):
        self.__videoDownloader = videoDownloader

    # access control
    # log requests 

    def downloadVideo(self, videoName):
        
        if videoName in self.__cache:
            print("*** Cached Video ***")
            return self.__cache[videoName]
        else:
            video = self.__videoDownloader.downloadVideo(videoName)
            self.__cache[videoName] = video
            return video
         

if __name__ == "__main__":

    objVideoDownloader = TPVideoDownloader()
    proxy = Proxy(objVideoDownloader)

    song1 = proxy.downloadVideo("Swami Bhajan: Gajavadana")
    print(song1)
    song2 = proxy.downloadVideo("Swami Bhajan: Muraliganalola")
    print(song2)
    song3 = proxy.downloadVideo("Imagine Dragons: Believer")
    print(song3)
    song4 = proxy.downloadVideo("Swami Bhajan: Gajavadana")
    print(song4)




