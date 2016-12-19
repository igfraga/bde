# bbl

list(APPEND sources
    "bblb/bblb_schedulegenerationutil.cpp"
    "bblb/bblb_schedulegenerationutil.h"
    "bbldc/bbldc_basicactual360.cpp"
    "bbldc/bbldc_basicactual360.h"
    "bbldc/bbldc_basicactual365fixed.cpp"
    "bbldc/bbldc_basicactual365fixed.h"
    "bbldc/bbldc_basicbasicdaycountadapter.cpp"
    "bbldc/bbldc_basicbasicdaycountadapter.h"
    "bbldc/bbldc_basicdaterangedaycountadapter.cpp"
    "bbldc/bbldc_basicdaterangedaycountadapter.h"
    "bbldc/bbldc_basicdaycount.cpp"
    "bbldc/bbldc_basicdaycount.h"
    "bbldc/bbldc_basicdaycountutil.cpp"
    "bbldc/bbldc_basicdaycountutil.h"
    "bbldc/bbldc_basicisdaactualactual.cpp"
    "bbldc/bbldc_basicisdaactualactual.h"
    "bbldc/bbldc_basicisma30360.cpp"
    "bbldc/bbldc_basicisma30360.h"
    "bbldc/bbldc_basicnl365.cpp"
    "bbldc/bbldc_basicnl365.h"
    "bbldc/bbldc_basicpsa30360eom.cpp"
    "bbldc/bbldc_basicpsa30360eom.h"
    "bbldc/bbldc_basicsia30360eom.cpp"
    "bbldc/bbldc_basicsia30360eom.h"
    "bbldc/bbldc_basicsia30360neom.cpp"
    "bbldc/bbldc_basicsia30360neom.h"
    "bbldc/bbldc_calendarbus252.cpp"
    "bbldc/bbldc_calendarbus252.h"
    "bbldc/bbldc_calendardaterangedaycountadapter.cpp"
    "bbldc/bbldc_calendardaterangedaycountadapter.h"
    "bbldc/bbldc_calendardaycountutil.cpp"
    "bbldc/bbldc_calendardaycountutil.h"
    "bbldc/bbldc_daterangedaycount.cpp"
    "bbldc/bbldc_daterangedaycount.h"
    "bbldc/bbldc_daycountconvention.cpp"
    "bbldc/bbldc_daycountconvention.h"
    "bbldc/bbldc_perioddaterangedaycountadapter.cpp"
    "bbldc/bbldc_perioddaterangedaycountadapter.h"
    "bbldc/bbldc_perioddaycountutil.cpp"
    "bbldc/bbldc_perioddaycountutil.h"
    "bbldc/bbldc_periodicmaactualactual.cpp"
    "bbldc/bbldc_periodicmaactualactual.h"
    "bbldc/bbldc_terminatedbasicdaycountadapter.cpp"
    "bbldc/bbldc_terminatedbasicdaycountadapter.h"
    "bbldc/bbldc_terminateddaterangedaycountadapter.cpp"
    "bbldc/bbldc_terminateddaterangedaycountadapter.h"
    "bbldc/bbldc_terminateddaycountutil.cpp"
    "bbldc/bbldc_terminateddaycountutil.h"
    "bbldc/bbldc_terminatedisda30360eom.cpp"
    "bbldc/bbldc_terminatedisda30360eom.h"
    "bblscm/bblscm_version.cpp"
    "bblscm/bblscm_version.h"
    "bblscm/bblscm_versiontag.cpp"
    "bblscm/bblscm_versiontag.h"
)
source_group("" FILES ${sources})

add_library(bbl STATIC ${sources})

target_include_directories(bbl PUBLIC
    bblb
    bbldc
    bblscm
)

target_link_libraries(bbl PUBLIC
    bdl
    bsl
)
