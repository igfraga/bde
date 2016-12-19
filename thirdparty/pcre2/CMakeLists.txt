# pcre2

list(APPEND sources
    "pcre2_auto_possess.c"    
    "pcre2_chartables.c"    
    "pcre2_compile.c"    
    "pcre2_config.c"    
    "pcre2_context.c"    
    "pcre2_dfa_match.c"    
    "pcre2_error.c"    
    "pcre2_jit_compile.c"    
    "pcre2_maketables.c"    
    "pcre2_match.c"    
    "pcre2_match_data.c"    
    "pcre2_newline.c"    
    "pcre2_ord2utf.c"    
    "pcre2_pattern_info.c"    
    "pcre2_serialize.c"    
    "pcre2_string_utils.c"    
    "pcre2_study.c"    
    "pcre2_substitute.c"    
    "pcre2_substring.c"    
    "pcre2_tables.c"    
    "pcre2_ucd.c"    
    "pcre2_valid_utf.c"    
    "pcre2_xclass.c"
)
source_group("" FILES ${sources})

add_library(pcre2 STATIC ${sources})

target_include_directories(pcre2 PUBLIC . )

target_compile_definitions(pcre2 PUBLIC
    "PCRE2_CODE_UNIT_WIDTH=8"
    "HAVE_CONFIG_H"
    "SUPPORT_UNICODE"
)

