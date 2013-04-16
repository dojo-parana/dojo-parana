#!/usr/bin/env perl
use warnings;
use strict;

use Test::More;

#is(1, 2, "teste");

my $um =
"   ". 
"  |".
"  |";

my $dois =
" _ " .
" _|" .
"|_ ";

my $tres =
" _ " .
" _|" .
" _|";

my $doze =
"    _ \n" .
"  | _|\n" .
"  ||_ \n      ";


my $treze = 
"    _ \n" .
"  | _|\n" .
"  | _|\n      ";

sub parse {
    my $arg = shift(@_);

    if ($arg eq $dois) {
       return 2;
    }
    if ($arg eq $tres) {
       return 3;
    }   
    return 1;
}

sub splitArgs {
    my $arg = shift(@_);
    my @digitos = ('', '');

    
    my @linhas  = split("\n",$arg);

    for my $linha(@linhas){
        my $digito = 0;
        while ($linha =~ m/(.{3})/g){
             $digitos[$digito++] .= $1;
        }
    }

    return @digitos;
}

ok(parse($um) == 1, "um");
ok(parse($dois) == 2, "dois");
ok(parse($tres) == 3, "tres");

my @retorno_doze = ($um,$dois);
my @retorno_treze = ($um,$tres);

is_deeply(splitArgs($doze), @retorno_doze, "split 12");
is_deeply(splitArgs($treze), @retorno_treze, "split 13");

done_testing();

