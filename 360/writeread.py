import io
class WriteRead:
  '''Write Read Class'''
  def __init__(self):

  def write_output_file(self, o, line, printoutput=False):
    try:
      if printoutput == True:
        text = '{}'.format(line)
        print(text)
      o.write(line)
      o.write("\n")
    except IOError:
      raise