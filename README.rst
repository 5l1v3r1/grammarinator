=============
Grammarinator
=============
*ANTLRv4 grammar-based test generator*

.. image:: https://img.shields.io/pypi/v/grammarinator?logo=python&logoColor=white
   :target: https://pypi.org/project/grammarinator/
.. image:: https://img.shields.io/pypi/l/grammarinator?logo=open-source-initiative&logoColor=white
   :target: https://pypi.org/project/grammarinator/
.. image:: https://img.shields.io/travis/renatahodovan/grammarinator/master?logo=travis&logoColor=white
   :target: https://travis-ci.org/renatahodovan/grammarinator
.. image:: https://img.shields.io/coveralls/github/renatahodovan/grammarinator/master?logo=coveralls&logoColor=white
   :target: https://coveralls.io/github/renatahodovan/grammarinator

*Grammarinator* is a random test generator / fuzzer that creates test cases
according to an input ANTLR_ v4 grammar. The motivation behind this
grammar-based approach is to leverage the large variety of publicly
available `ANTLR v4 grammars`_.

The `trophy page`_ of the found issues is available from the wiki.

.. _`ANTLR v4 grammars`: https://github.com/antlr/grammars-v4
.. _`trophy page`: https://github.com/renatahodovan/grammarinator/wiki


Requirements
============

* Python_ >= 3.5
* pip_ and setuptools Python packages (the latter is automatically installed by
  pip).
* ANTLR_ v4

.. _Python: https://www.python.org
.. _pip: https://pip.pypa.io
.. _ANTLR: http://www.antlr.org


Install
=======

The quick way::

    pip3 install grammarinator

Or clone the project and run setuptools::

    python3 setup.py install


Usage
=====

As a first step, *grammarinator* takes an `ANTLR v4`_ grammar and creates a test
generator script in Python3. Such a generator can be subclassed later to
customize it further if needed.

Example usage to create a test generator::

    grammarinator-process <grammar-file(s)> -o <output-directory> --no-actions

.. _`ANTLR v4`: https://github.com/antlr/grammars-v4

**Notes**

Grammarinator uses the `ANTLR v4`_ grammar format as its input, which makes
existing grammars (lexer and parser rules) easily reusable. However, because
of the inherently different goals of a fuzzer and a parser, inlined code
(actions and conditions, header and member blocks) are most probably not
reusable, or even preventing proper execution. For first experiments with
existing grammar files, ``grammarinator-process`` supports the command-line
option ``--no-actions``, which skips all such code blocks during fuzzer
generation. Once inlined code is tuned for fuzzing, that option may be omitted.

After having generated and optionally customized a fuzzer, it can be executed
either by the ``grammarinator-generate`` script or by instantiating it
manually.

Example usage of ``grammarinator-generate``::

    grammarinator-generate <generator> -r <start-rule> -d <max-depth> \
    -o <output-pattern> -n <number-of-tests> \
    -t <transformer1> -t <transformer2>

**Notes**

Real-life grammars often use recursive rules to express certain patterns.
However, when using such rule(s) for generation, we can easily end up in an
unexpectedly deep call stack. With the ``--max-depth`` or ``-d`` options, this
depth - and also the size of the generated test cases - can be controlled.

Another speciality of the ANTLR grammars is that they support the so-called
hidden tokens. These rules typically describe such elements of the target
language that can be placed basically anywhere without breaking the syntax. The
most common examples are comments or whitespaces. However, when using these
grammars - which don't define explicitly where whitespace may or may not appear
in rules - to generate test cases, we have to insert the missing spaces
manually. This can be done by applying a serializer (with the ``-s``
option) to the tree representation of the output tests. A simple serializer -
that inserts a space after every unparser rule - is provided by grammarinator
(``grammarinator.runtime.simple_space_serializer``).

In some cases, we may want to postprocess the output tree itself (without
serializing it). For example, to enforce some logic that cannot be
expressed by a context-free grammar. For this purpose the transformer mechanism
can be used (with the ``-t`` option). Similarly to the serializers, it will
take a tree as input, but instead of creating a string representation, it is
expected to return the modified (transformed) tree object.

As a final thought, one must not forget that the original purpose of grammars
is the syntax-wise validation of various inputs. As a consequence, these
grammars encode syntactic expectations only, and not semantic rules. If we
still want to add semantic knowledge into the generated test, then we can
inherit custom fuzzers from the generated ones and redefine methods
corresponding to lexer or parser rules in ways that encode the required
knowledge (e.g.: HTMLCustomGenerator_).

.. _HTMLCustomGenerator: examples/fuzzer/HTMLCustomGenerator.py

Working Example
===============

The repository contains a minimal example_ to generate HTML files. To give it
a try, run the processor first::

    grammarinator-process examples/grammars/HTMLLexer.g4 \
    examples/grammars/HTMLParser.g4 -o examples/fuzzer/


Then, use the generator to produce test cases::

    grammarinator-generate HTMLCustomGenerator.HTMLCustomGenerator -r htmlDocument \
    -o examples/tests/test_%d.html -s HTMLGenerator.html_space_serializer -n 100 -d 20 --sys-path examples/fuzzer/

.. _example: examples/


Compatibility
=============

*grammarinator* was tested on:

* Linux (Ubuntu 16.04 / 18.04)
* Mac OS X (Sierra 10.12 / High Sierra 10.13 / Mojave 10.14 / Catalina 10.15)
* Windows (Server 2012 R2 / Server version 1809 / Windows 10)


Citations
=========

Background on *grammarinator* is published in (R. Hodovan, A. Kiss, T. Gyimothy:
"Grammarinator: A Grammar-Based Open Source Fuzzer", A-TEST 2018).


Copyright and Licensing
=======================

Licensed under the BSD 3-Clause License_.

.. _License: LICENSE.rst
