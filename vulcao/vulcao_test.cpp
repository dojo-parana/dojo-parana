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
    EXPECT_EQ (1, vulcao_init (1));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

