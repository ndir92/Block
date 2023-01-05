from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = 'media/images/')
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class Slider(models.Model):
   image = models.ImageField(upload_to = 'media/images/')
   title = models.CharField(max_length=300)
   #sub_title =models.CharField(max_length=25)
   
 
 
class DimAgroAssurance(models.Model):
    OffreuAssurance = models.CharField(max_length=300)
    TypeAssurance = models.CharField(max_length=300)
    CulturAssure = models.CharField(max_length=300)
    NivPrime = models.CharField(max_length=300)
   
   
   

def __str__(self):
        return self.NumAgroCommercial

class DimAgroCulture (models.Model):
    ZonProd_Cult = models.CharField(max_length=300)
    Cultur_Pratique = models.CharField(max_length=300)
	
    Type_Semence = models.CharField(max_length=300)
    CodeVarietesCultiv = models.IntegerField()
    VarieteCultive = models.CharField(max_length=300)
    Appro_Intrant_mat = models.CharField(max_length=300)
    Appro_Intrant_mat = models.CharField(max_length=300)
    SourcApprovisIntran = models.CharField(max_length=300)
    SourcApprovisSemenc = models.CharField(max_length=300)
    SourcApprovisEngrProdPhyto = models.CharField(max_length=300)
    SourcApprovisMatAgro = models.CharField(max_length=300)
    TypeAcquisIntran = models.CharField(max_length=300)
    TypeAcquisMat = models.CharField(max_length=300)
    TypeFertilisUtil = models.CharField(max_length=300)
    TypePesticidUtil = models.CharField(max_length=300)
    ModAcquisParcel = models.CharField(max_length=300)
 
    

 
def __str__(self):
        return self.ZonProd_Cult
    
    
class DimAgroFinance(models.Model):
    OffreServicFinance = models.CharField(max_length=300)
    DemandApport=  models.IntegerField()
    TypeGaranExige = models.CharField(max_length=300)
    LongProcedCredi=  models.IntegerField()
    DelaiRembourse = models.IntegerField()
     
def __str__(self):
        return self.OffreServicFinance 
    


class DimAgroOrganisation(models.Model):
    name_Organisation = models.CharField(max_length=300)
    TypeServicOfferOP = models.CharField(max_length=300)
    BesoinForm = models.CharField(max_length=300)
    ContrainGlobalAgro= models.CharField(max_length=300)
    ContrainMajFilier = models.CharField(max_length=300)
    InfrasStockCondition = models.CharField(max_length=300)
    FournisEmballag = models.CharField(max_length=300)
    
def __str__(self):
        return self.name_Organisation 
    
    
class DimAgroProduction(models.Model):
    Name_Production = models.CharField(max_length=300)
    ProdCultHiver = models.CharField(max_length=300)
    TypeSolExist= models.CharField(max_length=300)
    TypeDegradZonCultur = models.CharField(max_length=300)
    CauseDegrad = models.CharField(max_length=300)
    
    def __str__(self):
        return self.Name_Production 
    
class DimAgroVarieteCultive(models.Model):
    
    nameVarietesCultiv = models.IntegerField()
    Arachide = models.CharField(max_length=300)
    Arachide = models.CharField(max_length=300)
    Mil= models.CharField(max_length=300)
    Maïs = models.CharField(max_length=300)
    Niébé = models.CharField(max_length=300)
    Pastèque = models.CharField(max_length=300)
    Oignon = models.CharField(max_length=300)
    Tomate = models.CharField(max_length=300)
    Piment = models.CharField(max_length=300)
    Jaxaatou = models.CharField(max_length=300)
    Pomme_de_terre= models.CharField(max_length=300)
    Chou_Pomme = models.CharField(max_length=300)
    Mangue = models.CharField(max_length=300)
    Papaye= models.CharField(max_length=300)
    Citron = models.CharField(max_length=300)
    Orange= models.CharField(max_length=300)
    
    
    
def __str__(self):
            return self.nameVarietesCultiv
    