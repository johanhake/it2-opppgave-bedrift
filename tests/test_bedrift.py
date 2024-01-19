from ..src.bedrift import Ansatt, Leder, Bedrift

def test_bedrift_navn():
    bedrift = Bedrift("Foo")
    assert bedrift.navn == "Foo"

def test_leder():
    bedrift = Bedrift("Foo")
    leder = bedrift.legg_til_leder("Arne", 750000.)
    assert len(bedrift.ansatte) == 1
    assert leder.navn == "Arne"
    assert leder.lønn == 750000.

def test_ansatt():
    bedrift = Bedrift("Foo")
    leder = bedrift.legg_til_leder("Arne", 750000.)
    ansatt = bedrift.legg_til_ansatt("Lise", 400000., leder.navn)
    assert len(bedrift.ansatte) == 2
    assert ansatt.navn == "Lise"
    assert ansatt.lønn == 400000.

def test_leder_lønn():
    bedrift = Bedrift("Foo")
    leder = bedrift.legg_til_leder("Arne", 750000.)
    bedrift.legg_til_ansatt("Lise", 600000., leder.navn)
    assert len(leder.ansatte) == 1
    assert leder.lønn >= 600000*1.5
