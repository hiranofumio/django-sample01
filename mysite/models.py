from django.db import models

class Contents(models.Model):
    """コンテンツモデル"""
    class Meta:
        # テーブル名定義
        db_table = 'contents'
        
    # テーブルのカラムに対応するフィールド定義
    message = models.CharField(verbose_name='message', max_length=255)

    def __str__(self):
        return self.message
        