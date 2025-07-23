from django.db import models
from pgvector.django import VectorField , HnswIndex

class App(models.Model):
    app_id = models.TextField(null=True)
    csv = models.FileField(upload_to="data" , null=True)
    painpoints = models.TextField(null=True)
    drivers = models.TextField(null=True)

class embeded_store(models.Model):
    app_id = models.TextField(null=True)
    content = models.TextField()
    embedding = VectorField(
                    dimensions= 384 , 
                    null = True,
                    blank = True
                   )
    class Meta:
        indexes = [
            HnswIndex(
                name = "clip__ll4_vectors_index",
                fields=["embedding"],
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            )
        ]
    
    def __str__(self):
        return self.app_ip

    


    
    



