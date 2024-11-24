def all_variants(text):
    if not text:
        yield ""
        return
    for av in all_variants(text[1:]):
        yield av
    for nv in all_variants(text[1:]):
        yield text[0] + nv

a = all_variants("abc")
for i in a:
    print(i)


