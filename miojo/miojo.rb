#!/usr/bin/env ruby
#
# automatically created by Dojo Polyglot Environ on 2013-05-27 19:35:46
# https://github.com/afurlan/dojo-polyglot-environ

require "test/unit"

class Miojo
    def initialize
    end

    def preparo(cozimento, ampulheta1, ampulheta2)
        if cozimento == ampulheta1
            return ampulheta1
        else
            return ampulheta2
        end
        10
    end
end

class TestMiojo < Test::Unit::TestCase
    def test_initialize
        assert_not_nil(Miojo.new)
    end

    def test_default
        miojo = Miojo.new
        tempo = miojo.preparo(3, 5, 7)
        assert_equal(10, tempo)
    end

    def test_caso_trivial
       miojo = Miojo.new
       tempo = miojo.preparo(3, 3, 5)
       assert_equal(3, tempo)
    end

end
