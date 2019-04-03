import sqlite3
import sys
DATABASE_PATH = '../data/vocab.db'

class SqlTools():
    ## TODO NEEDS INIT??
    def createDatabase(self):
        print("foo")


    def openDatabase(self, dbname):
        #check if already open
        self.db = sqlite3.connect(dbname)
        self.cur = self.db.cursor()
        return self.cur

    def closeDatabase(self):
        #print("something")
        self.db.close()
    #TODO ADD FIELDS/REARRANGE
    def insertVocabWordList(self, table_name, headers, vocabword_list):
        header_string = '(' + ','.join(headers + ['ATTEMPTED', 'CORRECT', 'STARRED']) + ')'
        placeholders = '(' + ','.join(['?' for header in headers] + ['0', '0', '0']) + ')'
        command = 'INSERT INTO ' + table_name + header_string + ' VALUES ' + placeholders
        print(command)
        # (null,?,?,?,0,0,0)
        self.db.executemany(command, vocabword_list)
        self.db.commit()

    #TODO FIND A WAY TO CREATE A UNIQUE/STANDARDIZED TABLE NAME SEPERATE FROM DECKNAME
    def createTable(self, table_name):
        #c = self.db.cursor()
        c = self.cur
        # Check if table exists
        # try:
        #     c.execute('SELECT * FROM ' + tablename)
        #     print(c.fetchall())
        #     print("table exists, probably.")
        # except sqlite3.OperationalError:
        #     # Table must not exist
        #     # SEARCH FOR TABLE NAME AND DONT RUN IF FOUND!
        command = ("CREATE TABLE IF NOT EXISTS " + str(table_name) +
                   "(CARDNUM INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "DECKNAME CHAR,"
                   "STARRED INT,"
                   "VOCABULARY CHAR,"
                   "DEFINITION CHAR,"
                   "PRONUNCIATION CHAR,"
                   "CORRECT INT,"
                   "ATTEMPTED INT);")

        # Extend table to include
        self.db.execute(command)
        self.db.commit()
        print("table ", table_name, " created!")

    def dropTable(self,table_name):
        command = "DROP TABLE " + table_name + ";"
        self.db.execute(command)
        self.db.commit()


    #TODO MULTIPLE LANG SUPPORT
    def findVocab(self, hanzi):
        self.cur.execute("SELECT * FROM TEST WHERE HANZI = ?", (hanzi,))
        data= self.cur.fetchall()
        if len(data)==0:
            print('There is no component named %s'%hanzi)
        else:
            print('Component %s found with rowids %s'%(hanzi,','.join(map(str, next(zip(*data))))))

    def consolidateEntries(self):
        #I guess multiple words can have sepeate defintions and pronunciations, so look for words that only have
        # are completely identical meaning same hanzi, pinyin, definition.
        print("I guess find any conflicting entries(same hanzi) and then merge the definitions")

    # TODO
    #  When I inserted into the table before, I had a typo where it had no comma after PRONUNCIATION in the query,
    #  and it was complaining about 7 values being passed to the command because the hidden cardnum cell was still there
    # TODO CHANGE THIS FOR MULTIPLE LANG SUPPORT
    def CSVtoSQLDatabase(self, csvfile, tablename):
        '''This function will parse a CSV line where format is as follows:
        vocabulary word,pronunciation,definition1;definition2;etc.
        (hanzi),(pinyin),(English defn.)'''

        hanzi = ""
        pinyin = ""
        definition = ""
        file = open(csvfile, mode="r")
        self.createTable(tablename)

        #cardnum = 0
        for line in file:
            if (len(line) == 0):
                print("Empty Line!")
            elif (line[0] == '#'):
                print("Comment line!")
            else:
                pos0 = line.find(",")
                pos1 = line.find(",", pos0 + 1)
                hanzi = line[0:pos0]
                pinyin = line[pos0 + 1:pos1]
                definition = line[pos1 + 1:-1]
                tup = [(hanzi, pinyin, definition,0,0,0)]
                print(tup)
                self.cur.executemany('INSERT OR IGNORE INTO ' + tablename +
                                     '(HANZI, PINYIN, DEFINITION, STARRED, ATTEMPTED, CORRECT) VALUES (?,?,?,?,?,?)'
                                     , tup)
                #cardnum += 1
        file.close()
        self.db.commit()
        print("Finished importing", self.db.total_changes, "entries.")
