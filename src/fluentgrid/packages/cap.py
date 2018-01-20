# ./cap.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d6ef60c1198a01e2a7cbade1d6922c31b4db5137
# Generated 2018-01-18 12:29:20.301759 by PyXB version 1.2.4 using Python 2.7.12.final.0
# Namespace urn:oasis:names:tc:emergency:cap:1.2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1ad0920c-fc1d-11e7-9254-685d43543ef9')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:tc:emergency:cap:1.2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 19, 10)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d[-,+]\\d\\d:\\d\\d')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 26, 10)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Actual = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Actual', tag='Actual')
STD_ANON_.Exercise = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Exercise', tag='Exercise')
STD_ANON_.System = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='System', tag='System')
STD_ANON_.Test = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Test', tag='Test')
STD_ANON_.Draft = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Draft', tag='Draft')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 37, 10)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.Alert = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Alert', tag='Alert')
STD_ANON_2.Update = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Update', tag='Update')
STD_ANON_2.Cancel = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Cancel', tag='Cancel')
STD_ANON_2.Ack = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Ack', tag='Ack')
STD_ANON_2.Error = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 49, 10)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Public = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Public', tag='Public')
STD_ANON_3.Restricted = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Restricted', tag='Restricted')
STD_ANON_3.Private = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Private', tag='Private')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 68, 16)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.Geo = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Geo', tag='Geo')
STD_ANON_4.Met = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Met', tag='Met')
STD_ANON_4.Safety = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Safety', tag='Safety')
STD_ANON_4.Security = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Security', tag='Security')
STD_ANON_4.Rescue = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Rescue', tag='Rescue')
STD_ANON_4.Fire = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Fire', tag='Fire')
STD_ANON_4.Health = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Health', tag='Health')
STD_ANON_4.Env = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Env', tag='Env')
STD_ANON_4.Transport = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Transport', tag='Transport')
STD_ANON_4.Infra = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Infra', tag='Infra')
STD_ANON_4.CBRNE = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='CBRNE', tag='CBRNE')
STD_ANON_4.Other = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 87, 16)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.Shelter = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Shelter', tag='Shelter')
STD_ANON_5.Evacuate = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Evacuate', tag='Evacuate')
STD_ANON_5.Prepare = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Prepare', tag='Prepare')
STD_ANON_5.Execute = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Execute', tag='Execute')
STD_ANON_5.Avoid = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Avoid', tag='Avoid')
STD_ANON_5.Monitor = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Monitor', tag='Monitor')
STD_ANON_5.Assess = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Assess', tag='Assess')
STD_ANON_5.AllClear = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='AllClear', tag='AllClear')
STD_ANON_5.None_ = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 102, 16)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.Immediate = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Immediate', tag='Immediate')
STD_ANON_6.Expected = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Expected', tag='Expected')
STD_ANON_6.Future = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Future', tag='Future')
STD_ANON_6.Past = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Past', tag='Past')
STD_ANON_6.Unknown = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 113, 16)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.Extreme = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Extreme', tag='Extreme')
STD_ANON_7.Severe = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Severe', tag='Severe')
STD_ANON_7.Moderate = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Moderate', tag='Moderate')
STD_ANON_7.Minor = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Minor', tag='Minor')
STD_ANON_7.Unknown = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 124, 16)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.Observed = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Observed', tag='Observed')
STD_ANON_8.Likely = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Likely', tag='Likely')
STD_ANON_8.Possible = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Possible', tag='Possible')
STD_ANON_8.Unlikely = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Unlikely', tag='Unlikely')
STD_ANON_8.Unknown = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 144, 16)
    _Documentation = None
STD_ANON_9._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_9._CF_pattern.addPattern(pattern='\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d[-,+]\\d\\d:\\d\\d')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 151, 16)
    _Documentation = None
STD_ANON_10._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_10._CF_pattern.addPattern(pattern='\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d[-,+]\\d\\d:\\d\\d')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 158, 16)
    _Documentation = None
STD_ANON_11._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_11._CF_pattern.addPattern(pattern='\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d[-,+]\\d\\d:\\d\\d')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_pattern)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """CAP Alert Message (version 1.2)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifier'), 'identifier', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2identifier', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 16, 8), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}sender uses Python identifier sender
    __sender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sender'), 'sender', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2sender', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 17, 8), )

    
    sender = property(__sender.value, __sender.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}sent uses Python identifier sent
    __sent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sent'), 'sent', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2sent', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 18, 8), )

    
    sent = property(__sent.value, __sent.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2status', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 25, 8), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}msgType uses Python identifier msgType
    __msgType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'msgType'), 'msgType', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2msgType', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 36, 8), )

    
    msgType = property(__msgType.value, __msgType.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2source', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 47, 8), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scope'), 'scope', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2scope', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 48, 8), )

    
    scope = property(__scope.value, __scope.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'restriction'), 'restriction', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2restriction', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 57, 8), )

    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}addresses uses Python identifier addresses
    __addresses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addresses'), 'addresses', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2addresses', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 58, 8), )

    
    addresses = property(__addresses.value, __addresses.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2code', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 59, 8), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2note', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 60, 8), )

    
    note = property(__note.value, __note.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'references'), 'references', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2references', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 61, 8), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}incidents uses Python identifier incidents
    __incidents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'incidents'), 'incidents', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2incidents', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 62, 8), )

    
    incidents = property(__incidents.value, __incidents.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}info uses Python identifier info
    __info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'info'), 'info', '__urnoasisnamestcemergencycap1_2_CTD_ANON_urnoasisnamestcemergencycap1_2info', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 63, 8), )

    
    info = property(__info.value, __info.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __identifier.name() : __identifier,
        __sender.name() : __sender,
        __sent.name() : __sent,
        __status.name() : __status,
        __msgType.name() : __msgType,
        __source.name() : __source,
        __scope.name() : __scope,
        __restriction.name() : __restriction,
        __addresses.name() : __addresses,
        __code.name() : __code,
        __note.name() : __note,
        __references.name() : __references,
        __incidents.name() : __incidents,
        __info.name() : __info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 64, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2language', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 66, 14), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2category', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 67, 14), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'event'), 'event', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2event', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 85, 14), )

    
    event = property(__event.value, __event.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}responseType uses Python identifier responseType
    __responseType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseType'), 'responseType', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2responseType', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 86, 14), )

    
    responseType = property(__responseType.value, __responseType.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}urgency uses Python identifier urgency
    __urgency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'urgency'), 'urgency', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2urgency', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 101, 14), )

    
    urgency = property(__urgency.value, __urgency.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}severity uses Python identifier severity
    __severity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'severity'), 'severity', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2severity', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 112, 14), )

    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}certainty uses Python identifier certainty
    __certainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'certainty'), 'certainty', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2certainty', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 123, 14), )

    
    certainty = property(__certainty.value, __certainty.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}audience uses Python identifier audience
    __audience = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audience'), 'audience', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2audience', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 134, 14), )

    
    audience = property(__audience.value, __audience.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}eventCode uses Python identifier eventCode
    __eventCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventCode'), 'eventCode', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2eventCode', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 135, 14), )

    
    eventCode = property(__eventCode.value, __eventCode.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}effective uses Python identifier effective
    __effective = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effective'), 'effective', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2effective', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 143, 14), )

    
    effective = property(__effective.value, __effective.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}onset uses Python identifier onset
    __onset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onset'), 'onset', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2onset', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 150, 14), )

    
    onset = property(__onset.value, __onset.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}expires uses Python identifier expires
    __expires = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expires'), 'expires', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2expires', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 157, 14), )

    
    expires = property(__expires.value, __expires.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}senderName uses Python identifier senderName
    __senderName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'senderName'), 'senderName', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2senderName', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 164, 14), )

    
    senderName = property(__senderName.value, __senderName.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}headline uses Python identifier headline
    __headline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'headline'), 'headline', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2headline', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 165, 14), )

    
    headline = property(__headline.value, __headline.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2description', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 166, 14), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}instruction uses Python identifier instruction
    __instruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instruction'), 'instruction', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2instruction', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 167, 14), )

    
    instruction = property(__instruction.value, __instruction.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}web uses Python identifier web
    __web = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'web'), 'web', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2web', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 168, 14), )

    
    web = property(__web.value, __web.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contact'), 'contact', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2contact', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 169, 14), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2parameter', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 170, 14), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resource'), 'resource', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2resource', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 178, 14), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__urnoasisnamestcemergencycap1_2_CTD_ANON__urnoasisnamestcemergencycap1_2area', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 190, 14), )

    
    area = property(__area.value, __area.set, None, None)

    _ElementMap.update({
        __language.name() : __language,
        __category.name() : __category,
        __event.name() : __event,
        __responseType.name() : __responseType,
        __urgency.name() : __urgency,
        __severity.name() : __severity,
        __certainty.name() : __certainty,
        __audience.name() : __audience,
        __eventCode.name() : __eventCode,
        __effective.name() : __effective,
        __onset.name() : __onset,
        __expires.name() : __expires,
        __senderName.name() : __senderName,
        __headline.name() : __headline,
        __description.name() : __description,
        __instruction.name() : __instruction,
        __web.name() : __web,
        __contact.name() : __contact,
        __parameter.name() : __parameter,
        __resource.name() : __resource,
        __area.name() : __area
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 136, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}valueName uses Python identifier valueName
    __valueName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueName'), 'valueName', '__urnoasisnamestcemergencycap1_2_CTD_ANON_2_urnoasisnamestcemergencycap1_2valueName', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2), )

    
    valueName = property(__valueName.value, __valueName.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__urnoasisnamestcemergencycap1_2_CTD_ANON_2_urnoasisnamestcemergencycap1_2value', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __valueName.name() : __valueName,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 171, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}valueName uses Python identifier valueName
    __valueName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueName'), 'valueName', '__urnoasisnamestcemergencycap1_2_CTD_ANON_3_urnoasisnamestcemergencycap1_2valueName', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2), )

    
    valueName = property(__valueName.value, __valueName.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__urnoasisnamestcemergencycap1_2_CTD_ANON_3_urnoasisnamestcemergencycap1_2value', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __valueName.name() : __valueName,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 179, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}resourceDesc uses Python identifier resourceDesc
    __resourceDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resourceDesc'), 'resourceDesc', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2resourceDesc', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 181, 20), )

    
    resourceDesc = property(__resourceDesc.value, __resourceDesc.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mimeType'), 'mimeType', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2mimeType', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 182, 20), )

    
    mimeType = property(__mimeType.value, __mimeType.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'size'), 'size', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2size', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 183, 20), )

    
    size = property(__size.value, __size.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uri'), 'uri', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2uri', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 184, 20), )

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}derefUri uses Python identifier derefUri
    __derefUri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'derefUri'), 'derefUri', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2derefUri', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 185, 20), )

    
    derefUri = property(__derefUri.value, __derefUri.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}digest uses Python identifier digest
    __digest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'digest'), 'digest', '__urnoasisnamestcemergencycap1_2_CTD_ANON_4_urnoasisnamestcemergencycap1_2digest', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 186, 20), )

    
    digest = property(__digest.value, __digest.set, None, None)

    _ElementMap.update({
        __resourceDesc.name() : __resourceDesc,
        __mimeType.name() : __mimeType,
        __size.name() : __size,
        __uri.name() : __uri,
        __derefUri.name() : __derefUri,
        __digest.name() : __digest
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 191, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}areaDesc uses Python identifier areaDesc
    __areaDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'areaDesc'), 'areaDesc', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2areaDesc', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 193, 20), )

    
    areaDesc = property(__areaDesc.value, __areaDesc.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'polygon'), 'polygon', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2polygon', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 194, 20), )

    
    polygon = property(__polygon.value, __polygon.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}circle uses Python identifier circle
    __circle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'circle'), 'circle', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2circle', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 195, 20), )

    
    circle = property(__circle.value, __circle.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}geocode uses Python identifier geocode
    __geocode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geocode'), 'geocode', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2geocode', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 196, 20), )

    
    geocode = property(__geocode.value, __geocode.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altitude'), 'altitude', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2altitude', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 204, 20), )

    
    altitude = property(__altitude.value, __altitude.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}ceiling uses Python identifier ceiling
    __ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ceiling'), 'ceiling', '__urnoasisnamestcemergencycap1_2_CTD_ANON_5_urnoasisnamestcemergencycap1_2ceiling', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 205, 20), )

    
    ceiling = property(__ceiling.value, __ceiling.set, None, None)

    _ElementMap.update({
        __areaDesc.name() : __areaDesc,
        __polygon.name() : __polygon,
        __circle.name() : __circle,
        __geocode.name() : __geocode,
        __altitude.name() : __altitude,
        __ceiling.name() : __ceiling
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 197, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}valueName uses Python identifier valueName
    __valueName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueName'), 'valueName', '__urnoasisnamestcemergencycap1_2_CTD_ANON_6_urnoasisnamestcemergencycap1_2valueName', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2), )

    
    valueName = property(__valueName.value, __valueName.set, None, None)

    
    # Element {urn:oasis:names:tc:emergency:cap:1.2}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__urnoasisnamestcemergencycap1_2_CTD_ANON_6_urnoasisnamestcemergencycap1_2value', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __valueName.name() : __valueName,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })



valueName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2))
Namespace.addCategoryObject('elementBinding', valueName.name().localName(), valueName)

value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2))
Namespace.addCategoryObject('elementBinding', value.name().localName(), value)

alert = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alert'), CTD_ANON, documentation='CAP Alert Message (version 1.2)', location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 10, 2))
Namespace.addCategoryObject('elementBinding', alert.name().localName(), alert)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 16, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sender'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 17, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sent'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 18, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), STD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 25, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'msgType'), STD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 36, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 47, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scope'), STD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 48, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'restriction'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 57, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addresses'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 58, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 59, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 60, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'references'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 61, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'incidents'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 62, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'info'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 63, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 47, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 57, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 58, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 59, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 60, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 61, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 62, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 63, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 212, 8))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifier')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sender')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 17, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sent')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 18, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 25, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'msgType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 36, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 47, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scope')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 48, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'restriction')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 57, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addresses')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 58, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 59, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 60, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'references')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 61, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'incidents')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 62, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'info')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 63, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['http://www.w3.org/2000/09/xmldsig#'])), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 212, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), pyxb.binding.datatypes.language, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 66, 14), unicode_default='en-US'))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), STD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 67, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'event'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 85, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseType'), STD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 86, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'urgency'), STD_ANON_6, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 101, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'severity'), STD_ANON_7, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 112, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'certainty'), STD_ANON_8, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 123, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audience'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 134, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventCode'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 135, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effective'), STD_ANON_9, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 143, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onset'), STD_ANON_10, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 150, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expires'), STD_ANON_11, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 157, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'senderName'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 164, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'headline'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 165, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 166, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instruction'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 167, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'web'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 168, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contact'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 169, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), CTD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 170, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resource'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 178, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), CTD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 190, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 66, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 86, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 134, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 135, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 143, 14))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 150, 14))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 157, 14))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 164, 14))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 165, 14))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 166, 14))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 167, 14))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 168, 14))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 169, 14))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 170, 14))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 178, 14))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 190, 14))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 66, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 67, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'event')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 85, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 86, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'urgency')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 101, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'severity')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 112, 14))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'certainty')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 123, 14))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audience')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 134, 14))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventCode')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 135, 14))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effective')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 143, 14))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onset')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 150, 14))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expires')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 157, 14))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'senderName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 164, 14))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'headline')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 165, 14))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 166, 14))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instruction')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 167, 14))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'web')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 168, 14))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contact')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 169, 14))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 170, 14))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resource')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 178, 14))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'area')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 190, 14))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueName'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 138, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 139, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueName'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 173, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 174, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resourceDesc'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 181, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mimeType'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 182, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'size'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 183, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 184, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'derefUri'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 185, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'digest'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 186, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 183, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 184, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 185, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 186, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resourceDesc')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 181, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mimeType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 182, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'size')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 183, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uri')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 184, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'derefUri')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 185, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'digest')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 186, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'areaDesc'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 193, 20)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'polygon'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 194, 20)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'circle'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 195, 20)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geocode'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 196, 20)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altitude'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 204, 20)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ceiling'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 205, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 194, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 195, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 196, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 204, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 205, 20))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'areaDesc')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 193, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'polygon')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 194, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'circle')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 195, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geocode')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 196, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altitude')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 204, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ceiling')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 205, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueName'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 216, 2)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 217, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 199, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd', 200, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()

