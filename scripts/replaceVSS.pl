#!/usr/bin/perl 

#### Import Classes
use File::Copy;
use FileHandle;
####
#### Define constants
my $idPort = "id";
my $subckt = ".SUBCKT";
my $vss	= "vss";
##

my $file =$ARGV[0];

### OPEN INPUT FILE 
print "Convertir de 0 a $vss los subcircuitos del archivo $file ...\n";
open(my $fhi, '<',$file) or die "Archivo no encontrado";
open(my $fho, '+>',"temp-$file");
while(<$fhi>){
#I get the inputs
if(m/($subckt\s[A-Za-z0-9_]+\s)0(\s.+)/)
	{
	print $fho "$1$vss$2\n";
	#print $fho "--$_"; # comento la linea
	print "Cambiado: $_";
	} else {
	print $fho "$_";}

}
close($fhi);
close($fho);

#copy("temp-$file","$file");
#unlink "temp-$file";
# En vez de copiar y borrar, directamente renombro el archivo:
move ("temp-$file","$file");
