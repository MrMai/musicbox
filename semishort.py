import semicore
# shortcut functions

def gen_scale(scale, semikey): # does sum_semi and note_shift
    return semicore.note_shift(semicore.sum_semi(scale), semikey)

def gen_scale_print(scale, semikey): # does sum_semi, note_shift, normalize_24, and sort_order
    return semicore.sort_order(semicore.normalize_24(semicore.note_shift(semicore.sum_semi(scale), semikey)), 24)
