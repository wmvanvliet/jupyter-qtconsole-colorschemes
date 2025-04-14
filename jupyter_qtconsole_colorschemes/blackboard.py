"""
A Pygments_ style based on the blackboard theme of TextMate_.

.. _Pygments: http://pygments.org
.. _TextMate: https://macromates.com
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number
from pygments.token import Operator, String, Text, Error

white            = '#ffffff nobold noitalic'
bright_orange    = '#f26512 nobold noitalic'
yolk_yellow      = '#f8d734 nobold noitalic'
lemon_yellow     = '#BBF34E nobold noitalic'
bright_green     = '#62d04e nobold noitalic'
dark_green       = '#0B3222 nobold noitalic'
dark_red         = '#370B22 nobold noitalic'
medium_grey      = '#AEAEAE nobold noitalic'
really_dark_blue = '#0d152c nobold noitalic'
dark_blue        = '#181f35 nobold noitalic'
medium_blue      = '#172247 nobold noitalic'
light_blue       = '#84A7C1 nobold noitalic'
vivid_blue       = '#36428a nobold noitalic'

class BlackboardStyle(Style):
    color = white
    background_color = really_dark_blue
    highlight_color = vivid_blue

    styles = {
        Text: white,

        Keyword: yolk_yellow,
        Keyword.Constant: lemon_yellow,
        #Keyword.Declaration
        #Keyword.Namespace
        #Keyword.Pseudo
        #Keyword.Reserved
        Keyword.Type: light_blue,

        Name: white,
        #Name.Attribute
        Name.Builtin: light_blue,
        #Name.Builtin.Pseudo
        Name.Class: bright_orange,
        Name.Constant: lemon_yellow,
        #Name.Decorator
        Name.Entity: white,
        Name.Exception: light_blue,
        Name.Function: bright_orange,
        Name.Label: white,
        Name.Namespace: white,
        Name.Other: white,
        Name.Tag: white,
        #Name.Variable
        #Name.Variable.Class
        #Name.Variable.Global
        #Name.Variable.Instance

        #Literal
        #Literal.Date
        String: bright_green,
        #String.Backtick
        #String.Char
        String.Doc: medium_grey,
        #String.Double
        #String.Escape
        #String.Heredoc
        #String.Interpol
        #String.Other
        #String.Regex
        #String.Single
        #String.Symbol

        Number: lemon_yellow,
        #Number.Float
        #Number.Hex
        #Number.Integer
        #Number.Integer.Long
        #Number.Oct

        Operator: yolk_yellow,
        Operator.Word: yolk_yellow,

        #Punctuation

        Comment: medium_grey,
        #Comment.Multiline
        #Comment.Preproc
        #Comment.Single
        #Comment.Special

        #Generic
        #Generic.Deleted
        Generic.Emph: 'italic',
        #Generic.Error
        #Generic.Heading
        #Generic.Inserted
        #Generic.Output
        Generic.Prompt: medium_grey,
        Generic.Strong: 'bold',
        #Generic.Subheading
        Generic.Traceback: medium_grey,

        #Token
        #Token.Other
        Token.Prompt: medium_grey,
        Token.PromptNum: medium_grey,
        Token.OutPrompt: medium_grey,
        Token.OutPromptNum: medium_grey,
        Token.RemotePrompt: medium_grey,
        Token.RemotePromptNum: medium_grey,
    }
