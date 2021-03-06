import sys

# Thrift files are generated from
# ./src/main/java/edu/cmu/lti/oaqa/flexneuart/letor/external/protocol.thrift
#

from scripts.py_featextr_server.python_generated.protocol.ExternalScorer import Processor
from scripts.py_featextr_server.python_generated.protocol.ttypes import ScoringException

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from threading import Lock

SAMPLE_HOST = '127.0.0.1'
SAMPLE_PORT = 8080


class BaseQueryHandler:
    def __init__(self, exclusive=True):
        self.lock_ = Lock() if exclusive else None

    def getScoresFromParsed(self, query, docs):
        try:
            if self.lock_ is not None:
                with self.lock_:
                    return self.computeScoresFromParsedOverride(query, docs)
            else:
                return self.computeScoresFromParsedOverride(query, docs)
        except Exception as e:
            raise ScoringException(str(e))

    def getScoresFromRaw(self, query, docs):
        try:
            if self.lock_ is not None:
                with self.lock_:
                    return self.computeScoresFromRawOverride(query, docs)
            else:
                return self.computeScoresFromRawOverride(query, docs)
        except Exception as e:
            raise ScoringException(str(e))

    def textEntryToStr(self, te):
        arr = []
        for winfo in te.entries:
            arr.append('%s %g %d ' % (winfo.word, winfo.IDF, winfo.qty))
        return te.id + ' '.join(arr)

    def concatTextEntryWords(self, te):
        arr = []
        for winfo in te.entries:
            arr.append(winfo.word)
        return ' '.join(arr)

    # One or both functions need to be implemented in a child class
    def computeScoresFromParsedOverride(self, query, docs):
        raise ScoringException('Parsed fields are not supported by this server!')

    def computeScoresFromRawOverride(self, query, docs):
        raise ScoringException('Raw-text fields are not supported by this server!')


# This function starts the server and takes over the program control
def startQueryServer(host, port, multiThreaded, queryHandler):
    processor = Processor(queryHandler)

    transport = TSocket.TServerSocket(host=host, port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    if multiThreaded:
        print('Starting a multi-threaded server...')
        server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    else:
        print('Starting a single-threaded server...')
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    server.serve()
    print('done.')
