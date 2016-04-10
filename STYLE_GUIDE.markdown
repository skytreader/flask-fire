# Style Guide

I am writing this more as a reference for refactoring than an intro guide.
Whatever I have now does not have that much guidance when it comes to style,
unfortunately.

## HTML

Use `snake-case` but with dashes instead of underscores since it is faster to
type (no need to hold down shift) for identifiers

## CSS

Use `snake-case` but with dashes instead of underscores since it is faster to
type (no need to hold down shift) for identifiers

## JavaScript

Refer to [Google's style guide](https://google.github.io/styleguide/javascriptguide.xml).

Avoid reference to global variables, or assuming you can get a particular value
in a DOM element identified by a particular selector. As much as possible, all
global/DOM references are only in one place, e.g., `$(document).ready`.

Use `camelCasing` as opposed to `snake_case`. `SHOUT_FOR_CONSTANTS`. A possible
exception is if a particular data/field comes from a server query in which case
`snake_case` should be acceptable.

## Python

Follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

### SQLAlchemy

Always explicitly name foreign key constraints so that they are easily referred
to in migrations.

All foreign key references should, as much as possible, be named as
`<table-name>_<foreign-field>`. The hard rule is that it should be end with
the foreign field it is using as FK.

Foreign key fields should have a corresponding field in the model declared as
a [relationship](http://docs.sqlalchemy.org/en/latest/orm/relationships.html).

When declaring columns, explicitly specify both `default` and `server_default`.
The difference is that `default` is the value _Python_ automagically encounters
while `server_default` is the value _the database_ automagically sets.
