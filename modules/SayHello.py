class SayHello:
  def __init__(self, target = 'World'):
      self.target = target
  
  def Say(self):
    print(f'Hello, {self.target}!!!')
  
if __name__ == '__main__':
  app = SayHello()
  app.Say()
  app = SayHello('Someone')
  app.Say()