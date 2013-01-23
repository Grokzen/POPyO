# POPO

Plain Old Python Object - For Django


## What is it?

This is a small helper function that can be used to make it easier to bind values from a form to a object or model in Django.

The idea is from Play Frameworks implementation of POJO bindings in their Controllers where it is possible to automaticly bind form attributes to object properties.


## How do it work?

This is a minimal working example. Irellevant imports is omitted.

When calling the popo decorator you should bind a name to a class, the decorator will try to create a new object of that type and bind each attribute from the form to the corosponding attributes on that instance. In the HTML part each input in the form should bind to the set name in the popo decorator and then the attribute name. Example: name="foo.url" and it will bind to the object foo and its attribute url.

No consideration is taken if that attribute works there that is up to the author to ensure they fit.


## Limitations

Currently it only supports one level of objects and nested objects is not supported. It is not possible to specify in the html: name="foo.bar.RandomAttrib"


## Usage example

```
##############
# Django view Class

def formrender(request):
    return render_to_response("form.html", getContext({}), context_instance=RequestContext(request) )

class Foobar(models.Model):
    self.a = models.CharField(max_length=100)
    self.b = models.CharField(max_length=100)

class Barfoo(models.Model):
    self.url = models.CharField(max_length=100)
    self.verbosity = models.CharField(max_length=100)

from popo import popo

@popo(foo=Barfoo, bar=Foobar)
def formtest(request, *args, **kwargs):
    print(kwargs["foo"].url)
    print(kwargs["foo"].verbosity)
    print(kwargs["bar"].a)
    print(kwargs["bar"].b)
    return HttpResponse(simplejson.dumps({}), "application/json")


################
# HTML part

<html>
    <head>
    </head>
<body>
    <form action="/formtest/" method="post">
        {% csrf_token %}
        <input type="text" id="a" name="foo.url"> <br>
        <input type="text" id="b" name="foo.processor"> <br>
        <input type="text" id="c" name="foo.verbosity"> <br> 
        <br>
        <input type="text" id="d" name="bar.a"> <br>
        <input type="text" id="e" name="bar.b"> <br>
        <input type="submit" value="Send"> 
    </form>
</body>
```


## How to install

Note: It is recomended allways to use a virtual-enviroment when using pyKwalify

1. Download the release you want to install from a tag, latest stable build or the dev branch.
2. Run "pip install popo-x.x.x.tar.gz"
3. To use popo see the 


## Build from source

1. Download the release you want to install from a tag, latest stable build or the dev branch.
2. Run "make sdist"
3. To install run "pip install dist/popo-x.x.x.tar.gz"


## Install from source

1. Download the release you want to install from a tag, latest stable build or the dev branch.
2. Run "make install"


## POPO python dependencies

No dependencies


## Supported python version

 - Python 2.7.x - Yes
 - Python 3.1.x - (Not yet tested)
 - Python 3.2.x - (Not yet tested
 - Python 3.3.x - (Not yet tested)


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some features'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


## License

MIT.
