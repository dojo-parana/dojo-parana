// Google GTest Framework Example
// To COMPILE IT
// g++ vulcao_test.cpp -lgtest_main -pthread -o vulcao_test
// TO RUN
// ./vulcao_test
//
// TO FILTER TEST EXECUTION
// ./vulcao_test --gtest-filter=vulcaoTest.Init
//

#include "gtest/gtest.h"
#include "vulcao.cpp"

TEST (vulcaoTest, Init) {
    vulcao_init (8, 8, 5, 4, 0, 0);
    EXPECT_EQ ('*', mapa[0][0]);
}

TEST (vulcaoTest, Fumaca) {
    vulcao_fumaca();
    EXPECT_EQ (1, dia);
    EXPECT_EQ ('*', mapa[0][0]);
    EXPECT_EQ ('*', mapa[0][1]);
    EXPECT_EQ ('*', mapa[1][0]);
}
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

