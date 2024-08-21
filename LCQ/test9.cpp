#include <cmath>
#include <iostream>
#include <gtest/gtest.h>
#include <iomanip>

constexpr double TOLERANCE_MULT = 1e9;
int i = 0;
double roundToNearestInterval(double price, double interval)
{
    if (interval == 0)
        return 0;
    std::cout << ++i << std::endl;
    return std::round((price * TOLERANCE_MULT) / (interval * TOLERANCE_MULT)) * interval;
}

double sum(double a, double b)
{
    double res = a + b;
    std::cout << ++i << std::endl;
    return res;
}

TEST(RoundingTest, testRoundToNearestInterval)
{
    // Test rounding when the price is exactly halfway between two intervals
    EXPECT_DOUBLE_EQ(2.5, roundToNearestInterval(2.45, 0.5));

    // Test rounding with a very small interval
    EXPECT_DOUBLE_EQ(3.001, roundToNearestInterval(3.0012, 0.001));

    double price = 999999999.9999999;
    double interval = 0.0000001;

    // Using EXPECT_EQ will fail because of precision issues
    EXPECT_EQ(roundToNearestInterval(1.0, 0), 0);

    // Using EXPECT_DOUBLE_EQ will pass because it accounts for precision issues
    EXPECT_DOUBLE_EQ(roundToNearestInterval(price, interval), 999999999.9999999);
}

int main(int argc, char **argv)
{
    double price = 123456789.987654321;
    double interval = 0.0001;
    std::cout << std::fixed << std::setprecision(20) << 1.0/3 << std::endl;
    std::cout << (price * TOLERANCE_MULT) / (interval * TOLERANCE_MULT) << std::endl;
    std::cout << roundToNearestInterval(price, interval) << std::endl;

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
