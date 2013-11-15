use strict; use warnings;

use Test::More;

use FizzBuzz;

ok(!is_mod_3(1));
ok(is_mod_3(3));

ok(!is_mod_5(1));
ok(is_mod_5(5));

ok(!is_mod_3_and_5(1));
ok(is_mod_3_and_5(15));

is( fizzbuzz(3), "Fizz" );
is( fizzbuzz(5), "Buzz" );
is( fizzbuzz(15), "FizzBuzz" );
is( fizzbuzz(1), 1 );

for (1 .. 100){
  is( fizzbuzz($_));
}

done_testing;

