# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SfsManagermsg(models.Model):
    """
    管理者のメッセージテーブル(m_managermsg)
    """

    content     = models.TextField(_(u'内容'), null=False, blank=False)
    apply_begin = models.DateField(_(u'適用開始日'), null=False, blank=False)
    apply_end   = models.DateField(_(u'適用終了日'), null=False, blank=False)
    create_user = models.CharField(_(u'作成者'), max_length=100, null=False, blank=False)
    create_date = models.DateField(_(u'作成日'), null=False, blank=False, default=timezone.now)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_managermsg'
        verbose_name = _(u'管理者のメッセージ')
        verbose_name_plural = _(u'業務 : 管理者のメッセージ (%s)' % db_table)
        ordering = ['-id', ]
