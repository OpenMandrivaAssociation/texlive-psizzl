%global tl_name psizzl
%global tl_revision 69742

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.35
Release:	%{tl_revision}.1
Summary:	A TeX format for physics papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/psizzl
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PSIZZL is a TeX format for physics papers written at SLAC and used at
several other places. It dates from rather early in the development of
TeX82; as a result, some of the descriptions of limitations look rather
quaint to modern eyes.

