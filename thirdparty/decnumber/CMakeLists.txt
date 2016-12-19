# decnumber

list(APPEND sources
    "decContext.c"
    "decDouble.c"
    "decPacked.c"
    "decQuad.c"
    "decSingle.c"
    "decNumber.c"
    "decimal128.c"
    "decimal64.c"
    "decimal32.c"
)
source_group("" FILES ${sources})

add_library(decnumber STATIC ${sources})

target_include_directories(decnumber PUBLIC . )

target_compile_definitions(decnumber PUBLIC
    "PCRE2_CODE_UNIT_WIDTH=8"
    "HAVE_CONFIG_H"
    "SUPPORT_UNICODE"
)

