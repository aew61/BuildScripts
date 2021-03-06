# if( MSVC )
#     set( SECURITY_FLAGS "/guard /GS /NXCOMPAT /analyze" )
#     set( SECURITY_LINKER_FLAGS "/SAFESEH /NXCOMPAT /DYNAMICBASE" )
# else()
#     set( SECURITY_FLAGS "" )
#     set( SECURITY_LINKER_FLAGS "" )
# endif()
set( SECURITY_FLAGS "" )
set( SECURITY_LINKER_FLAGS "" )

# if CLCACHE exists...set that to be the compiler

set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${SECURITY_FLAGS} /WX /EHa /Zi /sdl" CACHE STRING "c++ flags" )
set( CXX_FLAGS "{CXX_FLAGS} ${SECURITY_FLAGS} /WX /EHa /Zi /sdl" CACHE STRING "c++ flags" )

set( CMAKE_EXE_LINKER_FLAGS " ${SECURITY_LINKER_FLAGS} /machine:X86" CACHE STRING "exe linker flags" )

# Debug
set( CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /Od /MDd /D_DEBUG" CACHE STRING "c debug flags" )
set( CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /Od /MDd /D_DEBUG" CACHE STRING "c++ debug flags")
set( CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} /DEBUG" CACHE STRING "exe linker debug flags" )
set( CMAKE_SHARED_LINKER_FLAGS_DEBUG "${CMAKE_SHARED_LINKER_FLAGS_DEBUG} /DEBUG" CACHE STRING "shared linker debug flags" )
set( CMAKE_MODULE_LINKER_FLAGS_DEBUG "${CMAKE_MODULE_LINKER_FLAGS_DEBUG} /DEBUG" CACHE STRING "module linker debug flags" )

# Release
set( CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /Od /MDd" CACHE STRING "c release flags" )
set( CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Od /MDd" CACHE STRING "c++ release flags")
set( CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /DEBUG /SAFESEH" CACHE STRING "exe linker release flags" )
set( CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /DEBUG" CACHE STRING "shared linker release flags" )
set( CMAKE_MODULE_LINKER_FLAGS_RELEASE "${CMAKE_MODULE_LINKER_FLAGS_RELEASE} /DEBUG" CACHE STRING "module linker release flags" )
