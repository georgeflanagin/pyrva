    """
    ***************************************************************
    (0)                  IF versus TRY
    ***************************************************************

     (a) I am a curmudgeon who hates "if" ....
     (b) I hate "else" even more intensely
     (c) The following explains why.


                    George Flanagin
                    Computer Scientist
                    University of Richmond
                    gflanagi@richmond.edu

                    me+pyrva@georgeflanagin.com         """










    """
    (1) This was the as written code.  get() returns the value of
    a dictionary key if it exists, otherwise None.

    - If self.config is not a dictionary, get() will blow up.
    - If self.config is a defaultdict(#), get() may return
        whatever the default value is.
    """
    if self.config.get('proxy'):
        self.proxies = { 'https': self.config['proxy'] }
    else:
        self.proxies = {}




    #  defaultdict-s are a subject for another day. Incredibly useful, but
    #   very lightly used by most new Python programmers.








    """
    (2) If you are going to use get() and test with if, you really
    need to supply the correct default value.

    - Of course, this does not defend against proxy's pre-existence in
        config, but having a value that is False.
    """
    if self.config.get('proxy', None):
        self.proxies = { 'https': self.config['proxy'] }
    else:
        self.proxies = {}















    """
    (3) The correct way to test if a key is in the dict is with
    the 'in' operator.

    - VERY SELDOM SHOULD YOU INITIALIZE WITH A CONDITIONAL!
        Unfortunately, this if/else will wipe out any previous value
        of self.proxies. And the name is plural, so we would expect
        that it is going to have more than one proxy in proxies.
    - Again "in" might be redefined in a derived user type, and you
        may not want what __contains__ returns. "in" does work with
        defaultdict-s.
    """
    if 'proxy' in self.config:
        self.proxies = { 'https': self.config['proxy'] }
    else:
        self.proxies = {}










    """
    (4) Initialize it first!
    """
    self.proxies = {}
        ....
    if 'proxy' in self.config:
        self.proxies['https'] = self.config['proxy']
    else:
        pass

















    """
    (4.1) Vartiation 1
    """
    self.proxies = {}
        ....
    if 'proxy' in self.config:
        self.proxies['https'] = self.config['proxy']
    else:
        self.proxies['https'] = localhost

















    """
    (4.2) Variation 2
    """
    self.proxies = {}
        ....
    if 'proxy' in self.config:
        self.proxies['https'] = self.config['proxy']
    # No else


















    """
    (4.3) Variation 3
    """
    self.proxies = {}
        ....
    self.proxies['https'] = localhost if proxy not in self.config else self.config['proxy']




















    """
    (5) Why bother with the "if" at all? Just try it and see
    what happens.
    """
    self.proxies = {}
        ....
    try:
        self.proxies['https'] = self.config['proxy']
    except:
        pass # or something more appropriate.
















    """
    (6) It does not hurt to be a little more specific ...
    """
    self.proxies = {}
        ....
    try:
        self.proxies['https'] = self.config['proxy']
    except KeyError as e:
        pass # or something more appropriate.

















