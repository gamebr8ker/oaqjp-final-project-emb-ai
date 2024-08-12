import unittest

from emotion_detection import emotion_detector

class Testemotion_detection(unittest.TestCase):
    def test_statement_joy(self):
        statement = 'I am glad this happened'
        self.assertEqual( emotion_detector(statement)['dominant_emotion'], 'joy' )

    def test_statement_anger(self):
        statement = 'I am really mad about this'
        self.assertEqual( emotion_detector(statement)['dominant_emotion'], 'anger' )

    def test_statement_disgust(self):
        statement = 'I feel disgusted just hearing about this'
        self.assertEqual( emotion_detector(statement)['dominant_emotion'], 'disgust' )

    def test_statement_sadness(self):
        statement = 'I am so sad about this'
        self.assertEqual( emotion_detector(statement)['dominant_emotion'], 'sadness' )

    def test_statement_fear(self):
        statement = 'I am really afraid that this will happen'
        self.assertEqual( emotion_detector(statement)['dominant_emotion'], 'fear' )


if __name__ == '__main__':
    unittest.main()