package FizzBuzz;

use strict;
use warnings;

use Exporter 'import';

our @EXPORT = qw/is_mod_3 is_mod_5 is_mod_3_and_5 fizzbuzz/;

sub is_mod_3 {
  my $input = shift;
  return $input % 3 == 0;
}

sub is_mod_5 {
  my $input = shift;
  return $input % 5 == 0;
}

sub is_mod_3_and_5 {
  my $input = shift;
  return is_mod_3($input) and is_mod_5($input);
}

sub fizzbuzz {
  my $input = shift;
  return "Fizz" if is_mod_3( $input ) 
	and ! is_mod_5( $input );
  return "Buzz"if is_mod_5( $input) and ! is_mod_3($input);
  return "FizzBuzz" if is_mod_3_and_5($input);
  return $input;
}



1;

