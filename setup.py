from distutils.core import setup
setup(
  name = 'BSU',         # How you named your package folder (MyLib)
  packages = ['BSU'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A combination of brawl stars utilities',   # Give a short description about your library
  author = 'peanutbuttermurmite',                   # Type in your name
  author_email = 'example@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/peanutbuttermurmite/BSU',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'selenium'
  ],
  classifiers=[
