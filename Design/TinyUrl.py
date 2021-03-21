class Codec:
    def __init__(self):
        self.counter = 0
        self.urlToTinyUrlMapping = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL by assigning a new incremental integer to the URL.
        """
        hashValue = self.getHashValue(longUrl)
        self.urlToTinyUrlMapping[hashValue] = longUrl
        return "http://tinyurl.com/" + str(hashValue)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        encodedPart = shortUrl.split("/")[-1]
        return self.urlToTinyUrlMapping[int(encodedPart)]

    def getHashValue(self, s):
        """
        Here the hash code is generated only based on integer. Hence it has hold max int numbers of urls. For a better
        TinyURL system a better hashcode should be implemented.
        """
        return self.counter + 1


# Your Codec object will be instantiated and called as such:
codec = Codec()
tinyUrl = codec.encode("https://leetcode.com/problems/design-tinyurl")
print (tinyUrl)
print (codec.decode(tinyUrl))