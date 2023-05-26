@echo off

setlocal

call :runme call app\kit\kit.exe  --/rtx/ecoMode/enabled=false --ext-folder exts --enable robotica.service.video.thumbnail --enable omni.services.core --enable omni.services.transport.server.http --/exts/omni.kit.registry.nucleus/registries/0/name=kit/services --/exts/omni.kit.registry.nucleus/registries/0/url=https://dw290v42wisod.cloudfront.net/exts/kit/services %* <NUL

goto :eof

:runme
%*
goto :eof
