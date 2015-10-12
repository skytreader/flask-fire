module("Misc functions test", {});

test("capitalize test", function(assert){
    var asdf = "asdf";
    equals("Asdf", asdf.capitalize());

    var spacedOut = "spaced out";
    equals("Spaced out", spacedOut.capitalize());
});
