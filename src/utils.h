#ifndef _UTILS_H_
#define _UTILS_H_

#ifdef __GNUC__
#define ctz __builtin_ctz
#define popcount __builtin_popcount
#else
// Source: http://stackoverflow.com/a/5468852
#include <intrin.h>
static inline uint_fast32_t ctz(uint_fast32_t x)
{
	int r = 0;
	_BitScanForward(&r, x);
	return r;
}

// Source: http://stackoverflow.com/a/15979139
static inline uint_fast32_t popcount(uint_fast32_t v) {
	v = v - ((v >> 1) & 0x55555555);                // put count of each 2 bits into those 2 bits
	v = (v & 0x33333333) + ((v >> 2) & 0x33333333); // put count of each 4 bits into those 4 bits  
	return ((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;
}
#endif

// Source: http://stackoverflow.com/a/40357538
#ifdef _MSC_VER
#define INITIALIZER(f) \
	static void f();\
	static int __f1(){f();return 0;}\
	__pragma(data_seg(".CRT$XIU"))\
	static int(*__f2) () = __f1;\
	__pragma(data_seg())\
	static void f()
#elif __GNUC__
#define INITIALIZER(f) \
	__attribute__((constructor)) static void f()
#endif

#endif /* _UTILS_H_ */