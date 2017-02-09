# Header and source files
file(GLOB HAND_ISOMORPHISM_TEST_SOURCES *.c)

# Group source files for IDE source explorers (e.g. Visual Studio)
source_group("Source Files" FILES ${HAND_ISOMORPHISM_TEST_SOURCES})

add_executable(hand-isomorphism-test
	${HAND_ISOMORPHISM_TEST_SOURCES}
)
set_target_properties(hand-isomorphism-test PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(hand-isomorphism-test
	PRIVATE
		${PROJECT_SOURCE_DIR}/include/hand-isomorphism
		${PROJECT_SOURCE_DIR}/src
)
target_link_libraries(hand-isomorphism-test hand-isomorphism)

#set_target_properties(hand-isomorphism-test PROPERTIES C_STANDARD 99)
# C_STANDARD target property is only available since CMake 3.1,
# so we need this workaround to enable C99 on GNU compiler
if(CMAKE_COMPILER_IS_GNUCC)
	target_compile_options(hand-isomorphism-test PUBLIC "--std=c99")
endif()
