Title: Markdown reference
Latex:
Date: 2013-06-21 9:33
Category: Misc
Tags: coding, markdown 
Slug: markdown-reference
Author: Kristine Yu
Summary: Reference for markdown

### Headlines and horizontal rules

Headline depth can be indicated with #, e.g.

1. # H1, with '#'
2. ## H2, with '##'
3. ### H3, with '###'

Headlines for H1 and H2 can also be indicated with "underlining":

1. ==== for H1
2. ----- for H2

Horizontal rules can be indicated with 3+ of *, - or _:

***
---
___

#### Text formatting

##### Emphasis
Emphasized text can be indicated with * or _

1. Emphasized text looks like *this* or _this_
2. Strong text can be indicated with double * or _,
e.g. **this** or __this__
3. Strong and emphasized text can be indicate with triple asterisks,
***like this***

##### Blockquotes
Blockquotes can be indicated with >

> Here's a blockquote.

> Here's another blockquote.

### Lists

Items in itemized lists can be enumerated with +, -, * for unordered lists or with 1., 2., 3. for ordered lists.

* Item
* Item
* Item	

1. Item 1
2. Item 2
3. Item 3


* Item, followed by blank line

* Item with new paragraph


### Links

#### In-line link
    [link text](link "Optional title")
    [blog](http://www.krisyu.org "blog")

[Kristine's blog](http://www.krisyu.org "blog")

#### Referenced link

```markdown
[link text 1][link ref 1] and  [link text 2][link ref 2]
[link ref 1]: link url 1 "link title 1"
[link ref 2]: link url 2 "link title 2"
```

```markdown
Here's a link to [UMass Linguistics][1] and here's one to [UCLA
Linguistics][2]

    [1]: http://www.umass.edu/linguist "UMass Linguistics"
    [2]: http://www.linguistics.ucla.edu "UCLA Linguistics"
```

Here's a link to [UMass Linguistics][1] and here's one to [UCLA Linguistics][2]

[1]: http://www.umass.edu/linguist "UMass Linguistics"
[2]: http://www.linguistics.ucla.edu "UCLA Linguistics"


## Images

In-line images: 

```markdown
![Sideways kitties](/static/blog/img/2013/06/emmy-sophie-sideways.jpg "Emmy and Sophie")
```

![Sideways kitties](/static/blog/img/2013/06/emmy-sophie-sideways.jpg "Emmy
and Sophie")

Reference-style images: 

```markdown
    ![Young Indie][indie]
    ![Baby Hunter][hunter]

[indie]: /static/blog/img/2013/06/indie.jpg "Young Indie"
[hunter]: /static/blog/img/2013/06/hunter.jpg "Baby Hunter"
```

![Young Indie][indie]

![Baby Hunter][hunter]

[indie]: /static/blog/img/2013/06/indie.jpg "Young Indie"
[hunter]: /static/blog/img/2013/06/hunter.jpg "Baby Hunter"

# Codeblocks

[Syntax highlighting languages list](http://softwaremaniacs.org/media/soft/highlight/test.html)

# $\LaTeX$

```latex
$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$
```

$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$



